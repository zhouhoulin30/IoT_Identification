def identify(filename):
    import numpy as np
    import scipy
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeClassifier

    from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
    from sklearn.metrics import roc_curve, auc, roc_auc_score

    import matplotlib.pyplot as plt

    # 导入被动测量数据
    df1 = pd.read_csv("PassiveData.csv")
    # 表格所有数据共2267行
    df1.head(2267)
    # 导入未知数据集
    df2 = pd.read_csv(filename)
    # 测试数据共10行
    df2.head(10)
    # 统计各类样本数量
    # print(df.type.value_counts())
    y = df1.type
    y.head(2267)
    x = df1.drop('type', axis=1)
    x.head(2267)

    # 划分数据集
    seed = 5
    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.3, random_state=seed)
    z = df2.drop('type', axis=1)
    xtest = z[-10:]

    # 实例化
    rfc = RandomForestClassifier()
    # 用训练集数据训练模型
    rfc = rfc.fit(xtrain, ytrain)
    ytest = rfc.predict(xtest)

    # 导入测试集,rfc的接口score计算的时模型准确率accuracy
    # result = rfc.score(xtest, ytest)
    # print(result)

    # 输出结果
    # print('判定结果：%s' % ytest)
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    for i in range(len(ytest)):
        if ytest[i] == 1:
            count_1 = count_1 + 1
        elif ytest[i] == 2:
            count_2 = count_2 + 1
        elif ytest[i] == 3:
            count_3 = count_3 + 1
        elif ytest[i] == 4:
            count_4 = count_4 + 1
        elif ytest[i] == 5:
            count_5 = count_5 + 1
    percent_1 = count_1 / len(ytest)
    percent_2 = count_2 / len(ytest)
    percent_3 = count_3 / len(ytest)
    percent_4 = count_4 / len(ytest)
    percent_5 = count_5 / len(ytest)
    if percent_1 >= 0.7:
        return 1
    elif percent_2 >= 0.7:
        return 2
    elif percent_3 >= 0.7:
        return 3
    elif percent_4 >= 0.7:
        return 4
    elif percent_5 >= 0.7:
        return 5
    else:
        return 0