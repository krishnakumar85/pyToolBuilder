import Parser

print 'init'
gconfig = Parser.Config('..\\..\\config.txt')
gconfig.parse()
print 'done'
