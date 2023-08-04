# create_html_templates.py

# The number of HTML template files you want to create
num_templates = 40

# HTML template content
html_template = '''
{% extends 'courses/testing.html' %}
{% block content %}

{% endblock%}
'''

# Create HTML template files
for i in range(1, num_templates + 1):
    file_name = f'template_{i}.html'
    with open(file_name, 'w') as file:
        file.write(html_template.format(template_number=i))
    print(f'Created {file_name}')
