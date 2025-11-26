import nbformat

# Read the notebook
with open('Building the agent.ipynb', 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

# Write it back with proper formatting
with open('Building the agent.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)

print("Notebook cleaned and saved!")