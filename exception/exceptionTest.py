import logging
logging.basicConfig(level=logging.DEBUG)

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
    logging.debug('except:%s' % e)
finally:
    print('finally...')
print('END')


