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
    dot.attr(rankdir='TB', fontsize='12')

    node_style = {
        'shape': 'record',
        'fontname': 'Arial',
        'fontsize': '12',
        'fontcolor': 'black',
    }

    for class_name, details in classes.items():
        attributes = details.get('attributes', [])
        methods = details.get('methods', [])

        # Use raw strings to avoid the escape sequence warning
        attr_text = r'\l'.join(attributes) + r'\l' if attributes else ''
        method_text = r'\l'.join(methods) + r'\l' if methods else ''

        label = f"{{{class_name}|{attr_text}|{method_text}}}"
        dot.node(class_name, label=label, **node_style)

    for class_name, details in classes.items():
        parent = details.get('inherits')
        if parent:
            dot.edge(parent, class_name, arrowhead='onormal', fontsize='12')

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
