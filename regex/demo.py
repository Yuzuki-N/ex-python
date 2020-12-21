import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
noNewlineRegex = re.compile('.*')

print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)

print(newlineRegex.search('Serve the public trust.\nProtect the innocent. \nUphold the law.').group())