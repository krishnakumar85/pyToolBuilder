import Parser
import Logger

print 'initializing ' + __name__

gconfig = Parser.Config('../config.txt')
gconfig.parse()

glogger = Logger.Logger('..\log')

print 'done ' + __name__
