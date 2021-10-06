import os
#os.remove('astite.txt')
if os.path.exists('kaste.txt'):
    os.rename('kaste.txt', 'kastes.txt')
else:
    print('fails neeksitē')