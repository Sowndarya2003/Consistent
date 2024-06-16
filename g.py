def next_greater():
    arr=[12,14,2,16,5,3]
    n=len(arr)
    ans=[0]*n
    stack=[-1]
    for i in range (n-1,-1,-1):
        curr=arr[i]
        while stack.top()!=-1 and stack.top()>=curr:
            stack.pop()
        ans[i]=stack.top()
        stack.append(curr)
    return ans
next_greater()
