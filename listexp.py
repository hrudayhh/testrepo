catname=[]
while True:
	print('Enter cat name'+(str(len(catname)+1))+'or else enter nothing for exit')
	a=input()
	if a=='':
		print("enter your name first")
		break;
	catname=catname+[a] #list concatination
for i in catname:
	print(i)

