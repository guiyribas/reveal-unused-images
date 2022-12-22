import re
import os

# #
# This script should run in the same level that the root_directory
# #

# ---- change it according to your project ---- #
root_directory = 'root-folder'
output = []
output_aux = []
result = []

# get image used in js files
for path, subdirs, files in os.walk(root_directory):
    for name in files:
        if name.endswith(".js"):
            with open('{}/{}'.format(path, name), encoding='utf8') as html:
                content = html.read()
                pattern = r'[^\"\'=\s]+\.(?:jpe?g|png|PNG|gif|ico|pdf|svg)'
                matches = re.findall(pattern, content)
                output.extend(matches)

for out in output:
    output_aux.append(out.split('/')[-1])
for path, subdirs, files in os.walk(root_directory):
    for name in files:
        if not name.endswith('.js') and not name.endswith('.json') and name not in output_aux:
            result.append(name)

print(len(result))
print(result)
