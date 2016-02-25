import string

finput = open(r'/Users/ytjia/Downloads/tmp.txt')
foutput = open(r'/Users/ytjia/Downloads/offline_channel_id_comma.txt', 'w')
line = finput.readline()
record = line.split()
num = []
print len(record)
# print record
for i in record:
    idstr = string.join(record, ', ')
foutput.write(idstr)
    # foutput.write(', ')

finput.close()
foutput.close()
