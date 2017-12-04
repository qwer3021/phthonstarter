rmb_str_value = input('请输入人民币（cny）金额：')
# print(rmb_str_value)
usd_vs_rmb = 6.77
# 输入金额要用eval转化为数字
usd_value = eval(rmb_str_value) / usd_vs_rmb
# 用逗号隔开
print('美元金额：',usd_value)
