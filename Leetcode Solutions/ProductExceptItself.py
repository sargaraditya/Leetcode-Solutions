def productExceptSelf( nums):
    output = [1] * (len(nums))
    
    prefix = 1 
    postfix = 1

    for i in range(len(nums)):
        output[i] = prefix

        prefix *= nums[i]

        print(output)

    for i in range(len(nums)-1,-1,-1):
        output[i] *= postfix

        postfix *= nums[i]

        print(output)

    return output

nums = [1,2,3,4]
print(productExceptSelf(nums))