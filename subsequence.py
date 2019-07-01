def subsequence(arr,index,sub_seq):
	if index==len(arr):
		print(sub_seq)
		return 1
	else:
		first = subsequence(arr,index+1,sub_seq)
		second = subsequence(arr,index+1,sub_seq+[arr[index]])
		return first+second
print(subsequence([1,4,5],0,[]))