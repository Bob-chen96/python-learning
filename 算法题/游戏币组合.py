n = int(input('请输入游戏币个数：'))

m = int(input('请输入游戏币面值：'))
for i in range((m//n)+1):
    for j in range((m-10*i)+1):
        for k in range((m-10*i-5*j)+1):
              l = m-10*i-5*j-2*k
              if i+j+k+l == n and l>= 0:
                  print(i, j, k, l)


