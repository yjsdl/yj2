import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()




def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(img_name,"wb") as f:
		f.write(img_content)


def main():

	gevent.joinall([
			gevent.spawn(downloader,"1.jpg","https://anchorpost.msstatic.com/cdnimage/anchorpost/1077/f8/05865f2ff8ec42e55ffe3217f8a55e_1663_1610983689.jpg"),
			gevent.spawn(downloader,"3.jpg","https://anchorpost.msstatic.com/cdnimage/anchorpost/1041/d0/0c821e9039afe3bfe9358f090fcffd_1663_1607774835.jpg"),
			gevent.spawn(downloader,"2.jpg","https://anchorpost.msstatic.com/cdnimage/anchorpost/1003/60/d8fe78247c7229b9be220d6b457e8f_1663_1606665304.jpg")


	])

if __name__ == "__main__":
	main()
