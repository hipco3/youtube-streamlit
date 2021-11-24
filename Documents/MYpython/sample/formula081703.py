def ave_num(num1,num2,num3):
    return (num1+num2+num3)/3
div_result=ave_num(20,30,40)
text = "結果は{}です"
text2="結果は{}ではない"
if div_result >50:
    print(text.format(div_result))
else:
    print(text2.format(div_result))     