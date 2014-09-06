def main(css_file, fontpath, woff_file, ttf_file):
	import os, re
	from base64 import b64encode

	if os.path.isfile(css_file):
		woff_file = '/'.join([fontpath, woff_file])
		ttf_file =  '/'.join([fontpath, ttf_file])

		if os.path.isfile(woff_file) and os.path.isfile(ttf_file):
			css = open(css_file).read()
			woff = b64encode(open(woff_file).read())
			ttf = b64encode(open(ttf_file).read())

			css = re.sub(
				r'data:application/x-font-woff;charset=utf-8;base64,[^\)]*'
			,	'data:application/x-font-woff;charset=utf-8;base64,'+woff
			,	css)

			css = re.sub(
				r'data:application/x-font-ttf;charset=utf-8;base64,[^\)]*'
			,	'data:application/x-font-ttf;charset=utf-8;base64,'+ttf
			, 	css)

			print css

			return True
		else:
			print 'woff or ttf file not found'
			print woff_file
			print ttf_file

	return False

if __name__ == "__main__":
	import sys

	sys.exit(not main(*sys.argv[1:]))
