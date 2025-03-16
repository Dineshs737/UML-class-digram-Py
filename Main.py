from graphviz import Digraph
import os
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
    dot.attr(rankdir='TB', fontsize='12')  # Increased fontsize for better readability

    # Define styles for nodes with clearer font and larger size
    node_style = {
        'shape': 'record',
        'fontname': 'Arial',  # Changed font to Arial for better clarity
        'fontsize': '12',     # Increased font size
        'fontcolor': 'black', # Changed font color to black for contrast
    }

    # Create nodes for each class
    for class_name, details in classes.items():
        attributes = details.get('attributes', [])
        methods = details.get('methods', [])

        # Format attributes and methods for the UML
        attr_text = '\l'.join(attributes) + '\l' if attributes else ''
        method_text = '\l'.join(methods) + '\l' if methods else ''

        # Combine into a single label
        label = f"{{{class_name}|{attr_text}|{method_text}}}"
        dot.node(class_name, label=label, **node_style)

    # Add inheritance relationships
    for class_name, details in classes.items():
        parent = details.get('inherits')
        if parent:
            dot.edge(parent, class_name, arrowhead='onormal', fontsize='12')

    return dot

# Ensure Graphviz is properly installed
if not os.system("dot -V") == 0:
    raise EnvironmentError("Graphviz executable 'dot' not found. Please install Graphviz and ensure it is added to your system's PATH.")

# Generate UML diagram
dot = generate_uml(classes)

# Save and render the UML diagram
dot.render('uml_class_diagram', view=True)
