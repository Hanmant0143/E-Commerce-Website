# import os
# create_html_templates.py

# The number of HTML template files you want to create
num_templates = 40

# HTML template content
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Template {template_number}</title>
</head>
<body>
    <h1>This is HTML Template {template_number}</h1>
    <p>Replace this text with your content.</p>
</body>
</html>
'''

# Create HTML template files
for i in range(1, num_templates + 1):
    file_name = f'template_{i}.html'
    with open(file_name, 'w') as file:
        file.write(html_template.format(template_number=i))
    print(f'Created {file_name}')



#     # Delete HTML template files
# for i in range(1, num_templates + 1):
#     file_name = f'template_{i}.html'
#     if os.path.exists(file_name):
#         os.remove(file_name)
#         print(f'Removed {file_name}')
#     else:
#         print(f'{file_name} does not exist.')

