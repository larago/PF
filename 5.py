sum = reduce(lambda a, x: a+ x, [0,1,2,3,4])


sentences = [
                'Mary read a stroy to Sam and Isla',
                'Isla cuddled Sam',
                'Sam shortled.'
            ]

# sam_count = 0
# for sentence in sentences:
#     sam_count += sentence.count('Sam')

##PF

sam_count = reduce(lambda a,x: a + x.count('Sam'),
                    sentences, 0)

print sam_count