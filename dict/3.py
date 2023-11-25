d1 = {
	"Dog": "waf-waf"
}

d2 = {
	"Cat": "meow-meow"
}

for k, v in d2.items():
	d1[k] = v

print(d1)