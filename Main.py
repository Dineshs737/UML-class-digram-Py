import os
from graphviz import Digraph
from classes_data import classes  # Import the classes dictionary from the external file

def generate_uml(classes):
    """
    Generate a UML class diagram using Graphviz.

    Parameters:
    - classes: A dictionary where each key is the class name and the value is another dictionary with:
      - 'attributes': List of attributes (with types).
      - 'methods': List of methods (with return types and parameters).
      - 'inherits': (Optional) Name of the parent class for inheritance.

    Returns:
    - A Graphviz Digraph object representing the UML diagram.
    """
    dot = Digraph('UML Class Diagram', format='png')

    # Adjust graph attributes for A4 size (8.27 x 11.69 inches), high resolution, and increased font size
    dot.attr(rankdir='TB', fontsize='18', size='8.27,11.69', nodesep='1', dpi='300')  # Increased font size to 18

    # Define styles for nodes with bold font and larger font size
    node_style = {
        'shape': 'record',
        'fontname': 'Arial',
        'fontsize': '18',  # Increased font size to 18
        'fontcolor': 'black',
        'fontweight': 'bold',  # Set font weight to bold
    }

    # Create class nodes with attributes and methods
    for class_name, details in classes.items():
        attributes = details.get('attributes', [])
        methods = details.get('methods', [])

        # Use raw strings to avoid the escape sequence warning
        # Add a blank line for vertical spacing between attributes and methods
        attr_text = r'\l'.join(attributes) + r'\l' if attributes else ''
        method_text = r'\l'.join(methods) + r'\l' if methods else ''

        # Combine attributes and methods with a space for vertical gap
        label = f"{{{class_name}|{attr_text}|{method_text}}}"

        # Add the node with the formatted label
        dot.node(class_name, label=label, **node_style)

    # Add inheritance relationships
    for class_name, details in classes.items():
        parent = details.get('inherits')
        if parent:
            dot.edge(parent, class_name, arrowhead='onormal', fontsize='18')  # Increased font size in edges

    # Add associations only between User subclasses and related classes
    for class_name, details in classes.items():
        if class_name != "User":  # Only add edges for subclasses of User
            related_classes = details.get('related_classes', [])
            for related_class in related_classes:
                dot.edge(class_name, related_class, arrowhead='none', fontsize='18')  # Increased font size in edges

    return dot

# Ensure Graphviz is installed and working
if not os.system("dot -V") == 0:
    raise EnvironmentError("Graphviz executable 'dot' not found. Please install Graphviz and ensure it is added to your system's PATH.")

# Ensure the output folder exists, create it if not
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Generate the UML diagram
dot = generate_uml(classes)

# Save and render the UML diagram to the 'output' folder
output_path = os.path.join(output_dir, 'uml_class_diagram')  # Path to save the file
dot.render(output_path, view=True)

print(f"UML class diagram has been saved to {output_path}.png")
