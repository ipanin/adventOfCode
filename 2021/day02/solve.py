# from https://www.reddit.com/user/4HbQ/ 
h = d = a = 0

for x in open(0):
  match x.split():
    case 'forward', n:
      h += int(n)
      d += int(n)*a
    case 'up', n:
      a -= int(n)
    case 'down', n:
      a += int(n)

print(h*a, h*d)