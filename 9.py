'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

a + b + c = 1000
.
Find the product abc.
'''

def main():
  '''
  After solving these two equations:
  a2 + b2 = c2
  a + b + c = 1000
  It turned out that c's upper bound is 500, which means a,b will also be inside 500
  '''
  for c_item in range(1, 500):
    for b_item in range(1, 500):
      for a_item in range(1, 500):
        if ((a_item * a_item) + (b_item * b_item) == (c_item * c_item)) and \
          (a_item + b_item + c_item == 1000):
          return (a_item, b_item, c_item)

if __name__ == '__main__':
    (a, b, c) = main()
    print a*b*c
