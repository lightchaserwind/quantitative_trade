# 一、 初识量化交易（上）
量化交易核心概念

## 1、什么是量化交易
    量化思想

        例如：博彩公司如何设置赔率,才能保证稳赚不赔

    量化交易

        量化交易是指以先进的数学模型替代人为的主观判断，利用计算机技术从庞大的历史数据中海选能带来超额收益的多种“大概率”事件以制定策略，

        极大地减少了投资者情绪波动的影响，避免在市场极度狂热或悲观的情况下作出非理性的投资决策

    量化交易知识树

        (1)金融学

            金融工程、金融衍生品、会计学

        (2)数学

            概率论、统计学、博弈论

        (3)计算机技术

            计算机编程、机器学习、大数据

    量化交易发展历史

        （1）美国

            1952-现代投资理论基础

                1952年，美国经济学家Harry Markowitz提出现代投资组合理论，为现代投资奠定理论基础

            1964-CAPM诞生

                William Sharpe团队开发了现代金融学的基石-资本资产定价模型（CAPM）

            1982-诞生与成长

                量化交易之父西蒙斯创办文艺复兴科技公司,过去40年的年化收益率高达35

            2008-风云突变

                美国次贷危机,引起量化对冲基金管理规模显著下滑，从鼎盛时期的2500亿美元下降到500亿美元

            2011-美国量化元年

                2012年，高盛将600名交易员裁剪为2名

            至今-稳步发展

                目前，量化投资技术日趋成熟，在目前全部的投资比例中，量化投资约占50%

        （2）中国

            2004-国内第一只量化基金诞生

                2004年8月光大保德信量化核心基金发布

            2010-诞生期

                2010年4月16日，中国第一只股指期货沪深300股指期货（IF）上市，标志着中国做空机制和杠杆交易的启蒙

            2015-启蒙期

                2015年4月16日，中证500股指期货上市，意味着量化基金拥有更多的发挥空间，小股盘的对冲也更为便利

            2019-发展期

                2019年6月证监会推动了公募基金转融通业务指引；融券的放开与应用，使得量化可以真正实现多空策略

            至今-黄金期

                随着政策的放开(融资融券)，以及人工智能技术的应用，国内的量化交易进入黄金期。

                截至2021年，量化公墓基金超2000亿元，量化私募基金规模估算约1.5 万亿元



补充知识

:::info
**Sharpe比：**

<font style="color:rgb(15, 17, 21);">投资的“性价比”。</font><font style="color:#DF2A3F;">数值越高，说明在承担相同风险的情况下，获得的回报越好</font>

    - <font style="color:rgb(15, 17, 21);">夏普比率 > 1：</font>**<font style="color:rgb(15, 17, 21);">表现优秀</font>**
    - <font style="color:rgb(15, 17, 21);">夏普比率 > 2：</font>**<font style="color:rgb(15, 17, 21);">表现非常出色</font>**
    - <font style="color:rgb(15, 17, 21);">夏普比率 > 3：</font>**<font style="color:rgb(15, 17, 21);">顶级表现</font>**<font style="color:rgb(15, 17, 21);">，但也需警惕历史数据过拟合的可能</font>

<font style="color:#DF2A3F;">  
</font>

**CAPM：**

<font style="color:rgb(15, 17, 21);">把“风险”变成一个数字（β），然后算出“为了承担这个风险，至少该赚多少”。</font>

<font style="color:rgb(15, 17, 21);">简单理解：根据历史数据，大盘涨1%，这家公司股票涨1.5%，那么β就为1.5</font>

:::

## 2、量化交易VS主观交易
| **比较要素** | **量化交易** | **主观交易** |
| --- | --- | --- |
| 纪律性 | 无主观情绪影响 | 主观情绪化 |
| 精力 | 不知疲倦 | 受交易员精力影响 |
| 效率 | 秒级 | 最快30秒 |
| 系统性 | 多层次、多角度、多数据 | 艺术性较强 |
| 可控性 | 风险明确可控 | 不可控 |
| 可复制性 | 可无限复制 | 可复制性差 |


## 3、量化交易流程及分类
数据获取

数据清洗

策略编写

策略回测

策略优化

模拟盘交易

实盘交易





# 二、初识量化交易（下）
## 1.量化交易分类
量化交易：交易产品、盈利模式、策略信号

（1）交易产品

股票策略、CTA策略、期权策略、FOF策略

CTA策略主要是做波动的，可以做空

FOF策略是基金的组合

（2）盈利模式

单边多空策略：做多做空

套利策略：A涨B跌,B涨A跌。通过合理配置A/B保证稳赚（例如：博彩公司）

对冲策略 ：

| 策略类型 | 盈利来源 | 风险特征 | 形象比喻 |
| --- | --- | --- | --- |
| 单边多空 | 价格的方向性波动 | 高风险（怕判断错方向） | 冲浪者：浪来了就起飞，没浪就趴着。 |
| 套利策略 | 价格的定价偏差（价差回归） | 低风险（怕执行太慢或成本过高） | 搬运工：把便宜地方的货搬到贵的地方卖。 |
| 对冲策略 | 资产间的相对强弱（超额收益） | 中低风险（怕相关性失效） | 天平：不管船怎么晃，我只看天平哪头重。 |


（3）策略信号

多因子策略：

均值回归策略：

动量效益策略：

二八轮动策略：

海龟策略：

机器学习策略：



## 2.小结
量化交易定义及历史

量化交易VS主观交易

量化交易流程及分类



# 三、量化交易开发流程
## 1.量化交易总体开发流程
（1）数据获取

（2）数据清洗

（3）策略编写

（4）策略回测

（5）策略优化

（6）模拟盘交易

（7）实盘交易

## 2.各步骤详解
（1）数据获取

内容：行情数据、宏观数据、财务数据、舆情数据

方式：网站下载、客户端、三方API、爬虫

（2）数据清洗

场景：垃圾数据清除、空值填充、格式转换、数据对齐

类库：Numpy、Pandas

（3）策略编写

信号捕捉 ->交易 -> 建仓、平仓

（4）策略回测

回测参数设置 -> 策略实例化 -> 历史数据载入 ->

回测执行 -> 计算盈亏 -> 计算统计指标 -> 生成回测报告

（5）策略优化

重视交易费

注重风险，重视退出

优化无止境（不要把过多的时间放置到优化上）

（6）模拟盘交易

过去表现并不表示未来结果

至上半年以上

模拟盘稳定收益100%以上再考虑实盘交易

（7）实盘交易

做好第一年会输的准备

不急于扩大投资，增加杠杆（风险控制控制再控制）

心跳最重要（自己要像量化系统一样操作）

## 3.小结
量化交易7步骤

核心步骤小结



# 四、量化交易策略分类
本节主要介绍：

量化交易策略分类体系

交易产品相关量化策略盈利模式



## 1.交易产品
### （1）股票策略
股票策略盈利模式，通过股价的波动进行盈利

股票：股份公司为筹集资金而发行给各个股东作为持股凭证并借以取得<font style="color:#DF2A3F;">股息</font>和<font style="color:#DF2A3F;">红利</font>的一种有价证券

### （2）期权策略
期权与期货

期权：一种<font style="color:#DF2A3F;">选择权</font>，是一种能在<font style="color:#DF2A3F;">未来某特定时间</font>以<font style="color:#DF2A3F;">特定价格买卖</font>一定数量的<font style="color:#DF2A3F;">某种特定商品的权利</font>

期货：一种<font style="color:#DF2A3F;">标准化合约</font>，<font style="color:#DF2A3F;">期货交易所</font>统一制定的、约定在<font style="color:#DF2A3F;">未来的某一个确定的日期和地点</font>按照约定的条件<font style="color:#DF2A3F;">买卖一定数量和质量</font>的标的资产的<font style="color:#DF2A3F;">标准化合约</font>

案例：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1777019515094-918fb67a-7373-4642-bbd3-938d517d24e6.png" width="1210" title="" crop="0,0,1,1" id="u20ed98ec" class="ne-image">

期权策略的盈利模式

盈利模式：期权合约差价（常用）、到期行权收益

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1777019785719-669a5bb8-e5af-42b8-a28a-cb9cf8ee8518.png" width="1004" title="" crop="0,0,1,1" id="u5847e081" class="ne-image">

买入一份低行权认购期权，同时卖出一份高行权认购期权。



### （3）CTA策略
盈利模式：关注<font style="color:#DF2A3F;">价格趋势</font>获取利差

价格走势存在<font style="color:#DF2A3F;">反身性</font>，随着市场上涨或下跌的<font style="color:#DF2A3F;">趋势</font>得到加强，而认知上的<font style="color:#DF2A3F;">偏移</font>又会反映在市场上

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778057044451-1adde9cc-38e6-4aea-947e-6c8fee3ce0e0.png" width="1381" title="" crop="0,0,1,1" id="u57fd0c30" class="ne-image">



### （4）FOF策略
FOF：基金中的基金，是一种专门投资于其他投资基金的基金

通过<font style="color:#DF2A3F;">资产配置</font>来分散风险、平滑波动、改善组合收益风险比，从而优化投资者的持有体验。

尤其是在<font style="color:#DF2A3F;">震荡的市场</font>背景下，FOF产品的优势尤其明显。

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778057406867-7986f728-55ad-48c2-ab6b-610587c0b3a5.png" width="1364" title="" crop="0,0,1,1" id="uc9822635" class="ne-image">



### 小结
量化交易策略的3种分类体系

4种量化交易策略盈利模式

## 2.盈利模式
### （1）单边多空策略
<font style="color:#DF2A3F;">低价买进</font>，待股价出现<font style="color:#DF2A3F;">单边下跌</font>时卖出，赚取利差

通过<font style="color:#DF2A3F;">单边买入</font>或<font style="color:#DF2A3F;">单边卖出</font>实现盈利

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778057903812-e1746e13-6c71-456b-ac5c-9dced37c0a13.png" width="1257" title="" crop="0,0,1,1" id="u274c762f" class="ne-image">



### （2）套利策略
在金融市场利用某些<font style="color:#DF2A3F;">金融产品价格与收益率暂时不一致</font>的机会获得收益的策略

追求<font style="color:#DF2A3F;">无风险套利</font>，即价格变动所产生的无风险收益

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778058123422-351b0a0b-b283-4e48-84f1-099bed36e4a8.png" width="1281" title="" crop="0,0,1,1" id="u59562337" class="ne-image">



### （3）对冲策略
对冲：指特意减低另一项投资风险的<font style="color:#DF2A3F;">投资</font>。同时进行两笔<font style="color:#DF2A3F;">行情相关</font>、<font style="color:#DF2A3F;">方向相反</font>、<font style="color:#DF2A3F;">数量相当</font>、<font style="color:#DF2A3F;">盈亏相抵</font>的交易

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778058259926-d4d5a9ae-54ac-49b4-a26a-0187bf2bf3eb.png" width="1253" title="" crop="0,0,1,1" id="uc33a300e" class="ne-image">

对冲策略：在期货股票市场和股票市场同时进行<font style="color:#DF2A3F;">等量反向交易</font>，以锁定既得利润（或成本），通过抵消两个市场的损益来<font style="color:#DF2A3F;">规避股票市场的系统性风险</font>

<font style="color:#DF2A3F;">做多同时做空</font>，市场向上，赚取；市场向下，赚钱或少亏钱

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778058455924-71f9aefc-c391-44a6-b782-3be432f48f9d.png" width="1250" title="" crop="0,0,1,1" id="u1d1130e4" class="ne-image">

### 小结
盈利模式分类下的3种策略

3种策略的盈利模式

## 3. 策略信号
策略信号分类介绍

各量化策略定义及盈利模式

量化交易策略流程：信号捕捉->交易->建仓/平仓

策略信号：<font style="color:#DF2A3F;">交易信号</font>，买入或卖出的一系列特征

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778060350574-472bbdba-2597-4b69-a6db-4711bc000b9e.png" width="1291" title="" crop="0,0,1,1" id="u45dc72d6" class="ne-image">



### （1）多因子策略
找到某些和收益率最相关的指标，并根据该指标，建一个股票组合，期望该组合在未来一段时间跑赢或跑输指数

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778060454843-e4c06a0c-e5d7-46d8-94f4-d7dcf201b1ef.png" width="1328" title="" crop="0,0,1,1" id="u5360db52" class="ne-image">



### （2）交易模型
基于现代多学科众多理论，以及多种金融技术分析理论，具有普遍性，可盈利可量化可执行<font style="color:#DF2A3F;">交易系统</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778060699884-dd4e9ab4-c80f-43de-9620-cb73172dc3b6.png" width="1256" title="" crop="0,0,1,1" id="ufb7826bf" class="ne-image">

### （3）机器学习
从大量数据中找到某种规律，包括但<font style="color:#DF2A3F;">不局限于文本数据，图像数据</font>等，找到可盈利，可量化，可执行的策略信号



### 小结
策略信号定义及作用

3个策略信号流派及盈利模式



# 五、股票交易维度和概念
## 1.<font style="color:rgb(31, 31, 31);">股票基本概念</font>
### （1）股票投资好处
股票：<font style="color:#DF2A3F;">股份公司</font>为<font style="color:#DF2A3F;">筹集资金</font>而发行给各个股东作为<font style="color:#DF2A3F;">持股</font>凭证并借以取得<font style="color:#DF2A3F;">股息</font>和<font style="color:#DF2A3F;">红利</font>的一种<font style="color:#DF2A3F;">有价证券</font>

好处：分红、送股配股、交易收益、本金少、易变现、避免货币贬值



### （2）常见金融标的投资的风险与收益
<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778120922483-8b58e7d3-23c7-4be0-8d72-26e4880a1448.png" width="1278" title="" crop="0,0,1,1" id="uaec0d0ed" class="ne-image">



### （3）股票分类
蓝筹股、白马股、成长股、周期股、概念股



**蓝筹股：**中石化、中石油、宁德时代、茅台

经验业绩<font style="color:#DF2A3F;">长期稳定增长的大公司</font>，一般是<font style="color:#DF2A3F;">各个行业的龙头企业</font>，<font style="color:#DF2A3F;">市值在5000亿以上</font>，不管行业景气不景气都能赚到钱，一般都有比较稳定的<font style="color:#DF2A3F;">现金分红</font>。

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778121688223-20db8942-7597-4ee4-8948-0b9cd31ab1fe.png" width="1162" title="" crop="0,0,1,1" id="u2d48c263" class="ne-image">



**白马股：**海尔

长期业绩稳定、业绩成长性高，有较强的分配能力、分红不错，<font style="color:#DF2A3F;">市值在3000亿以下</font>，一般集中在<font style="color:#DF2A3F;">消费领域</font>。

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778121851612-f84b2c80-cc66-47f6-88d0-d7d17ef69be4.png" width="1135" title="" crop="0,0,1,1" id="ue26b7807" class="ne-image">



**成长股：**最近的芯片类、金融科技类

成长性高于白马股，公司正处于<font style="color:#DF2A3F;">高速发展</font>的阶段，<font style="color:#DF2A3F;">业绩增长远超整个行业</font>，一般为<font style="color:#DF2A3F;">有发展前景的中小公司</font>，以<font style="color:#DF2A3F;">高技术和科技类</font>的为主

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778121986891-fd1b8fbd-010b-4e82-ad14-b54510ee8a49.png" width="1119" title="" crop="0,0,1,1" id="ue1a7a921" class="ne-image">



**周期股：**

业绩随<font style="color:#DF2A3F;">经济周期</font>波动明显，多为工业基础原材料的<font style="color:#DF2A3F;">大宗商品、机械、造船等制造业，港口、远洋运输等航运业</font>以及<font style="color:#DF2A3F;">汽车、房地产</font>这样的非生活必需品行业

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778122286186-ed2b3d8a-70b6-4fcb-a7c9-2f1f4765c0e1.png" width="1074" title="" crop="0,0,1,1" id="u2de6411c" class="ne-image">



**概念股：**

具有<font style="color:#DF2A3F;">某种特别内涵</font>的股票，这一内涵通常会被当作一种选股和炒作题材，<font style="color:#DF2A3F;">成为股市的热点</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778122411968-257ca65a-b870-4d40-88fc-0ac67c2212a1.png" width="1135" title="" crop="0,0,1,1" id="u0549effd" class="ne-image">



### 小结
股票投资6种好处

金融标的投资的风险与收益

根据风险与收益股票分类

## 2.<font style="color:rgb(31, 31, 31);">股票行业分类</font>
### <font style="color:rgb(31, 31, 31);">1.行业分类</font>
#### <font style="color:rgb(31, 31, 31);">（1）中证行业分类</font>
<font style="color:rgb(31, 31, 31);">中证行业分类标准由中证指数公司2007年开始正式发布，现行版本为2021年12月修订。中证行业分类标准相对</font><font style="color:#DF2A3F;">“官方”</font><font style="color:rgb(31, 31, 31);">，更接近</font><font style="color:#DF2A3F;">监管行业分类，并同国际接轨</font>

<font style="color:#DF2A3F;"></font>

中证行业分类标准划分为四级，分别为一级、二级、三级和四级行业分类;分为<font style="color:#DF2A3F;">11个一级行业、35个二级行业、90余个三级行业及200余个四级行业</font>

<font style="color:#DF2A3F;"></font>

中证行业分类链接:

[https://www.csindex.com.cn/#/indices/family/list?index_](https://www.csindex.com.cn/#/indices/family/list?index_)series=2&custom=0&sharelndex=18



想法记录：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778124243279-d1f7c88e-9991-43c3-846d-a2b2fdc16591.png" width="1358" title="" crop="0,0,1,1" id="u47206eba" class="ne-image">

<font style="color:rgb(31, 31, 31);">获取收益率最高的行业，按这个50个样板量进行持仓，验证收益情况。</font>

<font style="color:rgb(31, 31, 31);">如何调仓？ 什么时候调仓？</font>

<font style="color:rgb(31, 31, 31);"></font>

#### <font style="color:rgb(31, 31, 31);">（2）申万行业分类</font>
<font style="color:rgb(31, 31, 31);">申万行业分类标准由申万宏源研究所发布，现行版本为2021年8月修订。申万行业分类标准相对</font><font style="color:#DF2A3F;">“务实”</font><font style="color:rgb(31, 31, 31);">，更接近</font><font style="color:#DF2A3F;">中国行业国情特征</font>

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">申万行业分类标准划分为三级，分别为一级、二级和三级行业分类;申万行业分类分为</font><font style="color:#DF2A3F;">31个一级行业、134个二级行业和346个三级行业</font>

<font style="color:rgb(31, 31, 31);"></font>

### <font style="color:rgb(31, 31, 31);">2.分类作用</font>
#### <font style="color:rgb(31, 31, 31);">（1）持续盈利</font>
<font style="color:rgb(31, 31, 31);">最近二十年内持续盈利，</font><font style="color:#DF2A3F;">食品饮料与医药生物行业</font>

#### <font style="color:rgb(31, 31, 31);">（2）传统行业</font>
<font style="color:rgb(31, 31, 31);">前十年表现出色，后十年表现不佳，</font><font style="color:#DF2A3F;">电气设备，采掘，有色金属，传统汽车，机械设备，钢铁</font>

#### <font style="color:rgb(31, 31, 31);">（3）新兴行业</font>
<font style="color:rgb(31, 31, 31);">前十年不怎么样，最近十年表现出色，</font><font style="color:#DF2A3F;">计算机，电子，新能源，家电</font>

#### <font style="color:rgb(31, 31, 31);">（4）表现不佳</font>
<font style="color:rgb(31, 31, 31);">最近二十年内缺乏盈利表现，</font><font style="color:#DF2A3F;">公用事业、纺织服装</font>

<font style="color:#DF2A3F;"></font>

### 小结
2种常用股票行业分类

股票行业分类作用



## <font style="color:rgb(31, 31, 31);">3.影响股价因素</font>
股价：股票的<font style="color:#DF2A3F;">交易价格</font>，与股<font style="color:#DF2A3F;">票的价值是相对的概念</font>。股票价值的真实含义是<font style="color:#DF2A3F;">企业资产的价值</font>。而股价的价值就等于<font style="color:#DF2A3F;">每股收益乘以市盈率</font>

影响因素：经济因素、政治因素、行业因素、企业自身因素、市场因素、心理因素



### 1.经济因素
主要指经济周期因素，经济衰退，股价随之下跌；经济繁荣，股价也随之上涨



美国经济周期与金融周期对照

阴影部分为美国经济紧缩时期

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778145894112-a9f9aa41-e8f4-4e53-b844-8940a1d8b590.png" width="586" title="" crop="0,0,1,1" id="ubd420dc5" class="ne-image">



### 2.政治因素
外交的改善会使有关跨国公司股价上升；战争使各国政治经济不稳，股价下跌，但会使军工行业股价上升



俄乌战争对长城汽车的影响

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778146304370-f1cb6e1c-f30f-4ac9-a2e1-2b80b7df858e.png" width="1182" title="" crop="0,0,1,1" id="u802df868" class="ne-image">



### 3.行业因素
行业在国民经济中地位的变更，发展前景和发展潜力，信心行业的冲击等都会影响相关股票的价格



个股股价随行业整体趋势波动

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778148028647-10a00f5f-d94e-46bf-8408-1d7311d3d876.png" width="639" title="" crop="0,0,1,1" id="u9a0d69f8" class="ne-image">



### 4.企业自身因素
企业的<font style="color:#DF2A3F;">经营业绩水平</font>，本身的<font style="color:#DF2A3F;">资产信用</font>，<font style="color:#DF2A3F;">股息红利</font>的设定，外来的<font style="color:#DF2A3F;">发展前景</font>等等都可以影响该企业股票价格变动



可口可乐的案例

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778202230147-7a655cf3-1cc8-43c1-9ca6-dd40abbb62df.png" width="1198" title="" crop="0,0,1,1" id="u29bda9a4" class="ne-image">



### 5.市场因素
这里的市场，指的是：交易市场和市场的供求关系

主要指市场交易状况、其他金融投资产品的表现、交易因素、供求关系等因素



市场交易影响股价异常波动

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778202449776-ab18e3ac-527f-46e1-92f0-1df16aead748.png" width="1174" title="" crop="0,0,1,1" id="u0b769ce6" class="ne-image">



### 6.心理因素
投资人在受到各个方面的影响后产生心理状态改变，往往导致情绪波动，判断事务，这是引起股价狂跌暴涨的重要因素



Luna币案例

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778202683140-a5be2cc7-2b54-470a-9e65-cad70c6ab015.png" width="569" title="" crop="0,0,1,1" id="u48fef7bf" class="ne-image">

投资人心理因素是造成<font style="color:#DF2A3F;">股价短期巨大波动</font>的主要因素



### 小结
6种影响股价因素

6种因素回顾

## <font style="color:rgb(31, 31, 31);">4.股票交易基础知识</font>
### <font style="color:rgb(31, 31, 31);">1.股票交易基础知识</font>
#### <font style="color:rgb(31, 31, 31);">（1）交易时间</font>
<font style="color:rgb(31, 31, 31);">周一至周五(法定节假日除外)</font>

<font style="color:#DF2A3F;">上午9:30~11:30 下午13:00~15:00</font>

<font style="color:#DF2A3F;">价格优先，时间优先</font>

#### <font style="color:rgb(31, 31, 31);">（2）竞价成交</font>
<font style="color:rgb(31, 31, 31);">上午9:15~9:25开盘集合竞价(成交量最大的价格)</font>

<font style="color:#DF2A3F;">上午9:30~11:30 下午13:00~14:57连续竞价</font>

<font style="color:rgb(31, 31, 31);">下午14:57~15:00收盘集合竞价(成交量最大的价格)</font>

#### <font style="color:rgb(31, 31, 31);">（3）交易单位</font>
<font style="color:rgb(31, 31, 31);">报价单位</font><font style="color:#DF2A3F;">股</font><font style="color:rgb(31, 31, 31);">，交易单位</font><font style="color:#DF2A3F;">手</font><font style="color:rgb(31, 31, 31);">，</font><font style="color:#DF2A3F;">100股=1手</font>

<font style="color:rgb(31, 31, 31);">股价变动单位最小为</font><font style="color:#DF2A3F;">0.01元</font>

#### （4）庄家与散户
庄家：能够影响金融证券市场行情的大户投资者

散户：股市种投入股市资金量较小的个人投资者

#### （5）换手率
某段时期内的成交量/发行总股数

表征该股票交易的活跃程度

10~50%非常活跃，低于1%非常不活跃

#### （6）PE
市盈率，(每股市场价格)/(每股税后利润)

PE越高，该企业越被高估;反之，该企业越被低估



### <font style="color:rgb(31, 31, 31);">2.K线</font>
<font style="color:rgb(31, 31, 31);">将各种股票</font><font style="color:#DF2A3F;">每日、每周、每月开盘价、收盘价、最高价、最低价等涨跌变化状况</font><font style="color:rgb(31, 31, 31);">，用图形方式表现出来，即蜡烛图</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778203444646-43ce7cb6-e88a-4e11-8a6b-4ce2a2a4df7e.png" width="1120" title="" crop="0,0,1,1" id="u512e682d" class="ne-image">



### <font style="color:rgb(31, 31, 31);">3.财务知识</font>
<font style="color:rgb(31, 31, 31);">ROE 越高越好</font>

<font style="color:rgb(31, 31, 31);">净利润 越高越好</font>

<font style="color:rgb(31, 31, 31);">成长性 （营业利润增长率、净利润增长率） 越高越好</font>

<font style="color:rgb(31, 31, 31);"></font>

### <font style="color:rgb(31, 31, 31);">小结</font>
<font style="color:rgb(31, 31, 31);">6个股票交易基础知识</font>

<font style="color:rgb(31, 31, 31);">K线基础知识</font>

<font style="color:rgb(31, 31, 31);">财务基础知识</font>



## <font style="color:rgb(31, 31, 31);">5.基本选股及量化思维</font>
### <font style="color:rgb(31, 31, 31);">（1）选股定义</font>
<font style="color:rgb(31, 31, 31);">选股：通过某种手段方式，提供给投资者</font><font style="color:#DF2A3F;">判断个股</font><font style="color:rgb(31, 31, 31);">的依据，帮助投资者</font><font style="color:#DF2A3F;">选定个股</font><font style="color:rgb(31, 31, 31);">的方法，选股是股票投资的</font><font style="color:#DF2A3F;">第一步</font>

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">选股作用：选股的好坏，决定能否赚到钱</font>

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">选股方法：</font><font style="color:#DF2A3F;">基本面选股</font>

<font style="color:rgb(31, 31, 31);"></font>

### <font style="color:rgb(31, 31, 31);">（2）基本面选股</font>
<font style="color:rgb(31, 31, 31);">基本面：通过分析一家上市公司在发展过程中所面临的</font><font style="color:#DF2A3F;">外部因素以及自身的因素</font><font style="color:rgb(31, 31, 31);">，来预测其未来的发展前景，并以此来判断该上市公司的股票是否值得买入</font>

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">外部因素：经济增长，财政政策，利率变化</font>

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">内部因素：经营状况，行业地位，财务状况</font>

<font style="color:rgb(31, 31, 31);"></font>

### <font style="color:rgb(31, 31, 31);">（3）估值方法</font>
<font style="color:rgb(31, 31, 31);">股票估值：</font><font style="color:#DF2A3F;">基本面选股</font><font style="color:rgb(31, 31, 31);">的</font><font style="color:#DF2A3F;">核心方法</font><font style="color:rgb(31, 31, 31);">。股票估值能帮助投资者发现现价价值被低估的股票，让他们低买高卖，从而获利。</font>

常用指标：每股收益、市盈率、毛利率、净资产收益率、资产负载率、净利润增速



每股收益：

<font style="color:#DF2A3F;">越高越好</font>，代表公司的盈利水平



市盈率：

<font style="color:#DF2A3F;">同行业市盈率越低越好</font>

14~30倍正常

大于30属于高估

50倍以上存在泡沫



毛利率：

<font style="color:#DF2A3F;">越高越好</font>

毛利率大于50%属于很不错的公司



净资产收益率：

代表公司盈利能力

<font style="color:#DF2A3F;">ROE长期保持在20%以上就是白马股</font>



资产负载率：

适中为好，最好在<font style="color:#DF2A3F;">10%~40%</font>

过高，容易暴雷

过低，发展保守



净利润增速：

代表公司未来成长能力

近3年平均增速在20%以上属于优质企业

<font style="color:#DF2A3F;">大约50%属于成长股</font>

<font style="color:#DF2A3F;"></font>

### 小结
选股定义及作用

基本面选股回顾

常用估值方法及指标



## <font style="color:rgb(31, 31, 31);">6.股票交易必懂</font>
### 1.择时
买入股票和卖出股票的时机





### 2.择时的作用
择时的好坏决定能够赚到多少钱



### 3.择时方法
技术分析：

从K线形态、成交量、均线、布林带、MACD、KDJ等方面出发分析，它们是反应股价变化的指标

常用工具：K线形态、成交量、均线、布林带、MACD、KDJ



#### （1）K线形态
K线图蕴含大量信息，能显示<font style="color:#DF2A3F;">股价的强弱</font>、<font style="color:#DF2A3F;">多空双方的力量对比</font>，是技术分析最常见的工具

K线示例

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778209760570-7e8dba99-0fe9-4b64-8f22-f86a184e31b7.png" width="1159" title="" crop="0,0,1,1" id="u7cba900b" class="ne-image">



#### （2）成交量
在股市中，成交量不仅可以反映出<font style="color:#DF2A3F;">买卖数量的变化</font>，还可以通过成交量看出<font style="color:#DF2A3F;">多空双方的力量变化</font>



成交量的示例：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778209947065-5f0b221d-d12d-4f3a-b0a5-2ca1bcb85c5d.png" width="1167" title="" crop="0,0,1,1" id="ude91a1d1" class="ne-image">



#### （3）均线
将某一段时间的收盘价之和除以该周期所得到的一根平均线。常用的参数有5日、10日、20日、30日、60日等



均线示例：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778210072451-506811e6-42c8-4ed5-a834-73bf1d16aca4.png" width="1144" title="" crop="0,0,1,1" id="u23cbfd18" class="ne-image">





#### （4）布林带
布林带是一种常用的技术指标，它由<font style="color:#DF2A3F;">三条轨道线</font>组成，其中上下两条线分别可以看成是<font style="color:#DF2A3F;">价格的压力线和支撑线</font>，在两条线之间是一条<font style="color:#DF2A3F;">价格平均线</font>

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778210207088-0b550d4b-4d4b-40ba-855c-e1ad7f1f071e.png" width="1192" title="" crop="0,0,1,1" id="u8260a8d0" class="ne-image">



#### （5）MACD
Moving Average Convergence/Divergence, 意为异同移动平均线。它刻画的是<font style="color:#DF2A3F;">股价变化的速度 </font>（加速度）

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778210359964-00074014-d805-4346-a687-a405434ac30b.png" width="1249" title="" crop="0,0,1,1" id="u051e6375" class="ne-image">



#### （6）KDJ
中文名叫随机指标。通过<font style="color:#DF2A3F;">价格波动的真实波幅来反映价格走势的强弱和超买超卖现象</font>，在价格尚未上升或下降之前发出买卖信号的一种技术分析指标,适用<font style="color:#DF2A3F;">于短期行情</font>走势分析

KDJ大于80超买  小于30超卖

#### 小结
择时定义 （选股决定你能否赚到钱，择时决定你能赚多少钱）

技术分析

6种常用技术分析工具





## <font style="color:rgb(31, 31, 31);">7.量化交易平台</font>
### 1.国内常见量化交易平台
量化交易平台：可为量化交易研发人员提供所需的<font style="color:#DF2A3F;">量化数据</font>、<font style="color:#DF2A3F;">策略框架</font>、<font style="color:#DF2A3F;">回测框架</font>、<font style="color:#DF2A3F;">交易接口</font>等功能，极大提高量化交易初学者的研发效率

国内常见平台：聚宽、掘金量化、BigQuant、米宽（RiceQuant）、交易开拓者（TradeBlazer）



### 2.聚宽量化交易平台简介
聚宽(JoinQuant)量化交易平台是为量化爱好者(宽客)量身打造的云平台,提供精准的回测功能、高速实盘交易接口、易用的API文档、由易入难的策略库,便于量化研发人员快速实现、使用自己的量化交易策略

特点：

时间久（数据时间久）

Tick级数据 （秒级数据）

多交易品种（港股、期货）

Python API

实盘交易

社区活跃



### 3.聚宽量化交易平台在线使用
账号注册->试用申请->新建策略->策略回测->模拟交易

joinquant.com



### 小结
国内常见量化交易平台

聚宽量化交易平台简介



# 六、股价分析实战
## 1.基于Numpy股价统计分析
### 1.数据样本说明
<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778223898332-cf6a0157-30f4-4067-bfa0-4fa8e846f5e0.png" width="1132" title="" crop="0,0,1,1" id="u70b03dab" class="ne-image">



### 2.股价常用指标说明
极差：

<font style="color:#DF2A3F;">越高说明波动越明显</font>

股价近期最高级的最大值和最小值的差值



成交量加权平均价格：

英文名VWAP(Volume-Weighted Average Price, 成交量加权平均价格)是一个非常重要的经济学量，代表着金融资产的“平均”价格



收益率：

简单收益率，相邻两个价格之间的变化率

对数收益率，指所有价格取对数后两两之间的差值



波动率：

<font style="color:#DF2A3F;">越高说明波动越明显</font>

波动率是对价格变动的一种衡量



年波动率：

对数波动率的标准差除以其均值，再除以交易日倒数的平方根，通常交易日取250天



月波动率：

对数收益率的标准差除以其均值，再乘以交易月的平方根，通常交易月取12月





数据文件：[股票行情数据000001SZ.csv](https://www.yuque.com/attachments/yuque/0/2026/csv/21971555/1778231668310-04dfbad6-dcad-4e80-94ce-3eeff4998b43.csv)



csv原始数据：

:::info
股票代码,交易日期,开盘价,最低价,最高价,收盘价,成交量

000001.SZ,2009/1/5,9.71,9.57,9.74,9.51,340827

000001.SZ,2009/1/6,10.3,9.8,10.43,9.73,635330

000001.SZ,2009/1/7,9.99,10.2,10.4,9.99,611960

000001.SZ,2009/1/8,9.6,9.75,9.76,9.5,392572

000001.SZ,2009/1/9,9.85,9.6,9.93,9.6,604457

000001.SZ,2009/1/12,9.86,9.78,10.08,9.67,415480

000001.SZ,2009/1/13,9.47,8.88,9.63,8.88,1730708

000001.SZ,2009/1/14,10.2,9.3,10.25,9.3,765325

000001.SZ,2009/1/15,10.3,10.01,10.6,9.97,895014

000001.SZ,2009/1/16,10.62,10.34,10.94,10.34,664370

000001.SZ,2009/1/19,11.11,10.65,11.35,10.65,936335

000001.SZ,2009/1/20,11.36,11.07,11.4,11.02,472975

000001.SZ,2009/1/21,11.79,11.15,12.2,11.1,824456

000001.SZ,2009/1/22,11.79,11.8,12,11.4,469410

000001.SZ,2009/1/23,11.64,11.58,11.93,11.58,345713

000001.SZ,2009/2/2,11.66,11.76,11.99,11.51,329749

000001.SZ,2009/2/3,11.95,11.66,12.06,11.6,368640

000001.SZ,2009/2/4,13.04,12.02,13.15,12.02,540952

000001.SZ,2009/2/5,12.8,13.07,13.2,12.63,373428

000001.SZ,2009/2/6,13.19,12.82,13.44,12.82,324698

:::



代码示例：

```python
import numpy as np
from unittest import TestCase


class TestNumpyStock(TestCase):
    """
    读取指定列
    numpy.loadtxt 常用关键字参数:
    1. fname 文件名；
    2. delimiter 分隔符；
    3. usecols 选取列（元组）；
    4. unpack 是否按列拆成多个数组；
    5. encoding、skiprows 处理 UTF-8 与表头。
    CSV 列: 股票代码,交易日期,开盘价,最低价,最高价,收盘价,成交量 → 索引 0..6
    """

    def testReadFile(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print(close_price, volume)
        # [ 9.71 10.3   9.99  9.6   9.85  9.86  9.47 10.2  10.3  10.62 11.11 11.36 11.79 11.79 11.64 11.66 11.95 13.04 12.8  13.19]
        # [ 340827.  635330.  611960.  392572.  604457.  415480. 1730708.  765325. 895014.  664370.  936335.  472975.  824456.  469410.  345713.  329749. 368640.  540952.  373428.  324698.]

    # 计算最大值与最小值（最高价序列、最低价序列）
    def testMaxAndMin(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        high_price, low_price = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(4, 5),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("high_price:", high_price.max())  # 13.44
        print("low_price:", low_price.min())    # 8.88


    # 极差：最高价序列与最低价序列各自的 peak-to-peak
    def testPtp(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        high_price, low_price = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(4, 5),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("max - min of high price:", np.ptp(high_price))  # 3.8099999999999987
        print("max - min of low price:", np.ptp(low_price))    # 3.9399999999999995

    # 计算成交里加权平均价格
    # 成交里加权平均价格，英文名WAP(Volume-Weighted Average Price，成交里加权平均价格)是一个非常重要的经济学里，代表着金融资产的"平均”价格
    # 成交量加权平均价格 VWAP ≈ sum(收盘价 * 成交量) / sum(成交量)
    def testAVG(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("avg_price:{}".format(np.average(close_price)))
        print("VWAP:{}".format(np.average(close_price, weights=volume)))
        # avg_price:11.0115
        # VWAP:10.768422980338055

    # 计算中位数  收盘价的中位数
    def testMedian(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("close_price median:{}".format(np.median(close_price)))
        # close_price median:10.864999999999998

    # 计算方差  收盘价的方差
    def testVar(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print("close_price variance:{}".format(np.var(close_price)))
        print("close_price variance:{}".format(close_price.var()))
        # close_price variance: 1.3352127499999997
        # close_price variance: 1.3352127499999997

    # 计算股票收益率、年波动率及月波动率
    # 波动率是对价格变动的一种度里，历史波动率可以根据历史价格数据计算得出。计算历史波动率时，需要用到对数收益率
    # 年波动率等于对数收益率的标准差除以其均值，再乘以交易日的平方根，通常交易日取250天
    # 月波动率等于对数收益率的标准差除以其均值，再乘以交易月的平方根。通常交易月取12月
    def testVolatility(self):
        file_name = "D:\workspaceQT\QT_Meteor\class6_1\股票行情数据000001SZ.csv"
        close_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        log_return = np.diff(np.log(close_price))

        annual_volatility = log_return.std() / log_return.mean() * np.sqrt(250)

        monthly_volatility = log_return.std() / log_return.mean() * np.sqrt(12)

        print("annual_volatility:{}".format(annual_volatility))
        print("monthly_volatility:{}".format(monthly_volatility))
        # annual_volatility:34.45147972091315
        # monthly_volatility:7.547941033030367
```



### 小结
数据样样本介绍

股价常用指标



## 2..基于Numpy股价均线实操
### 1.简单移动均线
卷积：卷积可用于描述过去作用对当前的影响。卷积是时空响应的叠加，可用做计算“滑动平均”

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778290158541-ce70ce12-0718-43b4-a463-ce729644088c.png" width="1293" title="" crop="0,0,1,1" id="u9c6f451b" class="ne-image">

简单移动均线：

一般用户分析时间序列上的股价趋势

计算股价与等权重的指示函数的卷积



<font style="color:#DF2A3F;">生成权重 -> 卷积运算 -> 均线可视化</font>

### 2.指数移动均线
历史数据的权重以指数速度衰减

计算股价与权重衰减的指示函数的卷积



<font style="color:#DF2A3F;">权重初始化 -> 权重衰减 -> 卷积运算 -> 均线可视化</font>



### 3.代码实现
```python
import numpy as np
import matplotlib.pyplot as plt

from unittest import TestCase

class TestNumpyMA(TestCase):

    def testSMA(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\class6_2\\股票行情数据000001SZ.csv"
        end_price, volume = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2, 6),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print(end_price)
        N = 5;
        weight = np.ones(N) / N
        print(weight)
        sma = np.convolve(weight, end_price)[N-1:-N+1]
        print(sma)
        plt.plot(sma, linewidth=5)
        plt.show()

    def testExp(self):
        x = np.arange(5)
        y = np.arange(10)
        print("x", x)
        print("y", y)
        print("""Exp x : {}""".format(np.exp(x)))
        print("""Exp y : {}""".format(np.exp(y)))
        print("""Linespace : {}""".format(np.linspace(-1, 0, 5)))


    def testEMA(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\class6_2\\股票行情数据000001SZ.csv"
        end_price = np.loadtxt(
            file_name,
            delimiter=",",
            usecols=(2),
            unpack=True,
            encoding="utf-8",
            skiprows=1
        )
        print(end_price)
        N = 5
        weight = np.exp(np.linspace(-1, 0, N))
        weight = weight / np.sum(weight)
        print(weight)
        ema = np.convolve(weight, end_price)[N-1 : -N+1]
        print(ema)

        t = np.arange(N-1, len(end_price))
        plt.plot(t, end_price[N-1:], lw=1.0)
        plt.plot(t, ema, lw=2.0)
        plt.show()
```



### 小结
简单移动均线

指数移动均线





## 3.基于Pandas股票时间序列分析实战
### 1.股票时间序列
时间序列：

<font style="color:#DF2A3F;">金融领域最重要的数据类型之一</font>

股价、汇率为常见的时间序列数据

趋势分析：

<font style="color:#DF2A3F;">主要分析时间序列在某一方向上持续运动</font>

在量化交易领域，我们通过统计手段对投资品的收益率进行时间序列建模，以此来预测未来的收益率并产生交易信号

序列相关性：

金融时间序列的一个最重要特征是序列相关性



### 2.Pandas时间序列函数
datetime：

时间序列最常用的数据类型，方便进行各种时间类型运算

loc:

Pandas中对DataFrame进行筛选的函数，相当于SQL中的where

groupby:

Pandas中对数据分组函数，相当于SQL中的GroupBy



### 3.代码
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from unittest import TestCase

class TestPandasStock(TestCase):

    # 读取文件
    def testReadFile(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])

        print(df.info())
        print("---------------------")
        print(df.describe())


    # 时间处理
    def testTime(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]

        df["date"] = pd.to_datetime(df["date"])

        df["year"] = df["date"].dt.year
        df["month"] = df["date"].dt.month

        print(df)


    # 最低收盘价
    def testCloseMin(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]

        print("""close min: {}""".format(df["close"].min()))
        print("""close min index: {}""".format(df["close"].idxmin()))
        print("""close min frame: {}""".format(df.loc[df["close"].idxmin()]))



    # 每月平均收盘价与开盘价
    def testMean(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]

        df["date"] = pd.to_datetime(df["date"])
        df["month"] = df["date"].dt.month

        print("""month close mean : {}""".format(df.groupby("month")["close"].mean()))
        print("""month open mean : {}""".format(df.groupby("month")["open"].mean()))

    # 计算涨跌幅
    # 涨跌幅今日收盘价减去昨日收盘价
    def testRipples_ratio(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]

        df["date"] = pd.to_datetime(df["date"])

        df["rise"] = df["close"].diff()
        df["rise_ratio"] = df["rise"] / df.shift(1)["close"]

        print(df)

```



### 总结
股票时间序列

Pandas时间序列函数



## 4.基于Pandas实现K线图
### 1.K线图
K线图蕴含大量信息，能显示<font style="color:#DF2A3F;">股价的强弱，多空双方的力量对比</font>，是技术分析最常见的工具

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778310331059-f5bfcf4a-dc78-47a5-b759-b2525d32da14.png" width="1156" title="" crop="0,0,1,1" id="u0b2b2891" class="ne-image">



**matplotlib:**

Matplotlib是一个Python的2D绘图库，它以各种硬拷贝格式和跨平台的交互式环境生成出版质量级别的图形



**mpl_finance:**

matplotlib finance是 python中可以用来画出蜡烛图.线图的分析工具，目前已经从matplotlib中独立出来



### 2.K线图实现
```python
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
from mpl_finance import candlestick2_ochl
import mplfinance as mpf
from unittest import TestCase

class TestPandasKLine(TestCase):

    # 读取股票数据，画出K线图
    def testKLineChart(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]

        fig = plt.figure()
        axes = fig.add_subplot(111)
        candlestick2_ochl(
            ax=axes,
            opens=df["open"].values,
            closes=df["close"].values,
            highs=df["high"].values,
            lows=df["low"].values,
            width=0.75,
            colorup='red',
            colordown='green'
        )
        plt.xticks(range(len(df.index.values)), df.index.values, rotation=30)
        axes.grid(True)
        plt.title("K-Line")
        plt.show()

    # K线图带交易量
    def testKLineByVolume(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]
        df = df[[ "date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index('date')

        my_color = mpf.make_marketcolors(
            up = 'red',
            down = 'green',
            wick = 'i',
            volume = {'up':'red', 'down':'green'},
            ohlc = 'i',
        )

        my_style = mpf.make_mpf_style(
            marketcolors = my_color,
            gridaxis = 'both',
            gridstyle = '-.',
            rc = {'font.family':'STSong'}
        )

        mpf.plot(
            df,
            type = 'candle',
            title = "K-LineByVolume",
            ylabel = "price",
            style = my_style,
            show_nontrading = False,
            volume = True,
            ylabel_lower = 'volume',
            datetime_format='%Y-%m-%d',
            xrotation = 45,
            linecolor = '#00ff00',
            tight_layout = False
        )

    # K线图带交易量及均线
    def testKLineByMA(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name, skiprows=[0])
        df.columns = ["stock_id", "date", "close", "open", "high", "low", "volume"]
        df = df[["date", "close", "open", "high", "low", "volume"]]
        df["date"] = pd.to_datetime(df["date"])
        df = df.set_index('date')

        my_color = mpf.make_marketcolors(
            up='red',
            down='green',
            wick='i',
            volume={'up': 'red', 'down': 'green'},
            ohlc='i',
        )

        my_style = mpf.make_mpf_style(
            marketcolors=my_color,
            gridaxis='both',
            gridstyle='-.',
            rc={'font.family': 'STSong'}
        )

        mpf.plot(
            df,
            type = 'candle',
            title = "K-LineByMA",
            mav = [5, 10], # 添加 5日 10日 均线
            ylabel = "price",
            style = my_style,
            show_nontrading = False,
            volume = True,
            ylabel_lower = 'volume',
            datetime_format='%Y-%m-%d',
            xrotation = 45,
            linecolor = '#00ff00',
            tight_layout = False
        )

```



### 小结
K线图

K线图实现



## 5.基于Matplotlib实战MACD
### 1.MACD介绍
Moving Average Convergence/Divergence，意为异同移动平均线。它刻画的是<font style="color:#DF2A3F;">股价变化的速度</font>。

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778312447822-db23af95-506e-42fa-b782-2050c8fc362c.png" width="1303" title="" crop="0,0,1,1" id="ud9238754" class="ne-image">



### 2.MACD算法
<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778312476312-441a5fca-fc79-4b93-a5a7-f25cc805812e.png" width="1159" title="" crop="0,0,1,1" id="u510447c3" class="ne-image">



### 3.MACD实现
**ewm:**

pandas中指数加权移动窗口函数

采用ewm函数+mean() 快捷计算MACD



**bar:**

Matplotlib柱状图函数，高效绘制MACD中的柱状图



代码：

```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mycolors
from matplotlib.collections import LineCollection, PolyCollection
from unittest import TestCase


class TestMACD(TestCase):

    def cal_macd(self, df, fastperiod=12, slowperiod=26, signalperiod=9):
        ewma12 = df['close'].ewm(span=fastperiod, adjust=False).mean()
        ewma26 = df['close'].ewm(span=slowperiod, adjust=False).mean()
        df['dif'] = ewma12 - ewma26
        df['dea'] = df['dif'].ewm(span=signalperiod, adjust=False).mean()
        df['bar'] = (df['dif'] - df['dea']) * 2
        return df

    def test_MAcD(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name)
        df.columns = ["stock_id","date","close","open","high","low","volume"]
        df = df[["date","close","open","high","low","volume"]]
        df["date"] = pd.to_datetime(df["date"])

        df_macd = self.cal_macd(df)
        print(df_macd)

        plt.figure()
        df_macd['dea'].plot(color="red", label='dea')
        df_macd['dif'].plot(color="blue", label='dif')
        plt.legend(loc='best')

        pos_bar = []
        pos_index = []
        neg_bar = []
        neg_index = []

        for index, row in df_macd.iterrows():
            if (row['bar'] > 0):
                pos_bar.append(row['bar'])
                pos_index.append(index)
            else:
                neg_bar.append(row['bar'])
                neg_index.append(index)

        # 大于0用红色表示
        plt.bar(pos_index, pos_bar, width=0.5, color='red')
        # 小于等于0则用绿色表示
        plt.bar(neg_index, neg_bar, width=0.5, color='green')
        major_index = df_macd.index[df_macd.index]
        major_xtics = df_macd['date'][df_macd.index]
        plt.xticks(major_index, major_xtics)
        plt.setp(plt.gca().get_xticklabels(), rotation=30)

        plt.grid(linestyle='-.')
        plt.title('000001平安银行MACD图')
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.show()
```



### 小结
MACD介绍

MACD算法

MACD实现





## 6.基于Matplotlib实现KDJ
### 1.KDJ介绍
KDJ中文名叫<font style="color:#DF2A3F;">随机指数</font>。通过<font style="color:#DF2A3F;">价格波动的真实波幅来反映价格走势的强弱和超买超卖现象</font>，在价格尚未上升或下降之前发出买卖信号的一种技术分析指标,适用于<font style="color:#DF2A3F;">短期行情</font>走势分析

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778317212325-1f78da1a-e063-476f-ad4c-6961d643141c.png" width="1142" title="" crop="0,0,1,1" id="u6ffcbf51" class="ne-image">





### 2.KDJ算法
<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778317227178-2812ed7f-30f9-48c6-b5f0-5ddf13f64074.png" width="1207" title="" crop="0,0,1,1" id="ud0332547" class="ne-image">



### 3.KDJ实现
**rolling**

Pandas中移动窗口函数

每个窗口都是指定的固定大小，快捷计算Ln与Hn



**expanding**

Pandas中扩展窗口函数

只设置最小的观测值数量，不固定窗口大小，实现累计计算，即不断扩展。

连用expanding().max() -> 创新高



```python
import pandas as pd
import matplotlib.pyplot as plt

from unittest import TestCase

class TestKDJ(TestCase):

    def cal_kdj(self, df):
        low_list = df["low"].rolling(9, min_periods=9).min()
        low_list.fillna(value=df['low'].expanding().min(), inplace=True)
        high_list = df["high"].rolling(9, min_periods=9).max()
        high_list.fillna(value=df['high'].expanding().max(), inplace=True)
        rsv = (df['close'] - low_list) / (high_list - low_list) * 100
        df['k'] = pd.DataFrame(rsv).ewm(com=2).mean()
        df['d'] = df['k'].ewm(com=2).mean()
        df['j'] = 3 * df['k'] - 2 * df['d']
        return df


    def test_kdj(self):
        file_name = "D:\\workspaceQT\\QT_Meteor\\股票行情数据000001SZ.csv"
        df = pd.read_csv(file_name)
        df.columns = ["stock_id","date","close","open","high","low","volume"]
        df = df[["date","close","open","high","low","volume"]]
        df["date"] = pd.to_datetime(df["date"])

        df_kdj = self.cal_kdj(df)
        print(df_kdj)

        plt.figure()
        df_kdj['k'].plot(color="red", label = 'k')
        df_kdj['d'].plot(color="yellow", label = 'd')
        df_kdj['j'].plot(color="blue", label = 'j')

        major_index = df_kdj.index[df_kdj.index]
        major_xticks = df_kdj['date'][df_kdj.index]
        plt.xticks(major_index, major_xticks)
        plt.setp(plt.gca().get_xticklabels(), rotation=30)

        plt.grid(linestyle='-.')
        plt.title('000001平安银行KDJ图')
        plt.rcParams['axes.unicode_minus'] = False
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.show()
        
```



### 小结
KDJ介绍

KDJ算法  rsv -> K -> D -> J

KDJ实现



# 七、量化策略编写
## 1.<font style="color:rgb(31, 31, 31);">策略核心</font>
### 1.策略框架
**框架：**

<font style="color:#DF2A3F;">初始化+策略函数（周期循环）</font>

**初始化：**

通过初始化函数设置基准。初始化函数在整个回测或者实盘操作过程中只被运行一次，用于<font style="color:#DF2A3F;">初始化全局变量</font>

:::info
函数：initialize(context)

context: Context对象，存放有当前的账号/股票持仓信息

示例：

def initialize(context):

# g为全局变量，设定标的股票为深交所的平安银行

g.security = "000001.XSHE"

:::

**策略函数：**

策略开始后，随着时间<font style="color:#DF2A3F;">周期重复执行你的交易策略</font>。

:::info
def handle_data(context, data):

#下单一千股

order(g.security, 1000)

#卖出八百股股:

order(g.security, -800)

:::



### 2.实用策略示例
初始化：

设定投资标的（平安银行）

设定策略运行周期（每日）

策略函数：

如果上一时间点价格高出五天平均价1%，则全仓买入

如果上一时间点价格低于五天平均价，则空仓卖出

(画出上一时间点价格)



聚宽平台代码：

```python
# 初始化函数：回测开始前只执行一次
def initialize(context):
    # 全局变量：指定要交易的股票（平安银行）
    g.security = '000001.XSHE'
    
    # 运行策略函数：每根K线触发一次（这里是日线，每天执行一次）
    run_daily(market_open, time='every_bar')

# 策略核心逻辑：每天自动执行一次
def market_open(context):
    # 取出要交易的股票代码
    security = g.security
    
    # 获取历史数据：最近5天的日线收盘价
    # 参数：股票代码, 天数, 数据周期, 需要获取的字段（这里只取收盘价）
    close_data = attribute_history(security, 5, '1d', ['close'])
    
    # 计算5日均线：把最近5天收盘价求平均值
    MA5 = close_data['close'].mean()
    
    # 获取当前价格：取最近一天（最后一行）的收盘价
    current_price = close_data['close'][-1]

    # 获取账户当前可用现金（能用来买股票的钱）
    cash = context.portfolio.available_cash
    
    # ===================== 交易规则 =====================
    # 买入条件：当前价格 > 1.01倍5日均线（向上突破）
    if current_price > 1.01 * MA5:
        # 用所有可用现金全仓买入这只股票
        order_value(security, cash)
        # 打印日志：记录买入操作
        log.info("买入 %s" % (security))
    
    # 卖出条件：当前价格 < 5日均线 并且 持有股票可卖出数量 > 0（有持仓才卖）
    elif current_price < MA5 and context.portfolio.positions[security].closeable_amount > 0:
        # 卖出全部持仓，目标持仓数量=0
        order_target(security, 0)
        # 打印日志：记录卖出操作
        log.info("卖出 %s" % (security))
    
    # 绘图：把当前股价记录到回测图表
    record(stock_price=current_price)
```



### 小结
策略框架

实用策略示例



## 2.<font style="color:rgb(31, 31, 31);">设置函数</font>
### 1.常用策略设置函数
**基准：**

设置业绩比较基准

set_benchmark(security)

**佣金/印花税：**

股票类每笔交易时的手续费为:买入时佣金万分之三，卖出时佣金万分之三加千分之一印花税

set_order_cost(cost, type, ref=None)

**滑点：**

真实的成交价格与下单时预期的价格的偏差

set_slippage(object,type=None, ref=None)

**成交量比例：**

根据实际行情限制每个订单的成交量

set_option('order_volume_ratio', value)

**动态复权模式：**

设置真实价格，建议开启

set_option('use_real_price', value)



### 2.代码示例
```python
# 初始化函数：回测开始前，只执行一次
def initialize(context):
    # 1. 设置策略业绩基准（对比曲线）：沪深300指数
    set_benchmark("000300.XSHG")
    
    # 2. 全局变量：指定交易股票为 平安银行(000001)
    g.security = '000001.XSHE'
    
    # 3. 设置每日运行时间：每天上午10:00自动执行 market_open 函数
    run_daily(market_open, time='10:00')
    
    # 4. 设置股票交易手续费（真实模拟交易成本）
    set_order_cost(
        OrderCost(
            open_commission=0.03,      # 买入佣金：万分之3（0.03%）
            close_commission=0.03,     # 卖出佣金：万分之3（0.03%）
            close_tax=0.01,            # 卖出印花税：千分之1（0.1%）
            min_commission=5           # 单笔佣金最低收费5元
        ), 
        type='stock'  # 手续费规则适用于股票
    )
    
    # 5. 滑点设置（已注释，不生效）：设置0.2%的价格相关滑点
    #set_slippage(PriceRelatedSlippage(0.002),type='stock')
    
    # 6. 订单比例设置（已注释，不生效）
    #set_option('order_volume_ratio',0.5)
    
    # 7. 关闭“使用真实价格”：回测使用回测系统默认价格撮合
    set_option('use_real_price', False)

# ==================== 每日交易逻辑 ====================
# 每天 10:00 执行一次
def market_open(context):
    # 判断：如果当前账户 没有持有 平安银行
    if g.security not in context.portfolio.positions:
        # 买入 1000 股 平安银行
        order(g.security, 1000)
    
    # 如果账户 已经持有 平安银行
    else:
        # 卖出 800 股 平安银行
        order(g.security, -800)
```



### 小结
常用策略设置函数

代码示例



## 3.<font style="color:rgb(31, 31, 31);">定时函数</font>
### 1.定时函数介绍
**定时函数：**

设定回测和模拟交易中运行时间及频率

**月度：**

run_monthly(func,monthday,time='open',reference_secuity)

**周度：**

run_weekly(func,weekday,time='open',reference_secuity)

**日度：**

run_daily(func,time='open',reference_secuity)



<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778468115203-efcf9c4a-504e-48a1-ad87-78d9b2edf27f.png" width="1240" title="" crop="0,0,1,1" id="u878b28ba" class="ne-image">



### 2.实战
```python
def initialize(context):
    # 设定业绩标的为“沪深300”
    set_benchmark("000300.XSHG")
    g.security = '000001.XSHE'
    # 定时交易
    #run_daily(market_open, time='10:00', reference_security='000300.XSHG')
    # 每分钟
    #run_daily(market_open, time='every_bar', reference_security='000300.XSHG')
    # 每月第一个交易日
    #run_monthly(market_open, 1, time='open')
    # 每周最后一个交易日
    run_weekly(market_open, -1, time='open')

def market_open(context):
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)
```





### 小结
定时函数介绍

代码示例





## 4.<font style="color:rgb(31, 31, 31);">交易函数</font>
### 1.交易函数
#### （1）交易数量
:::info
order(security, amount, style=None, side='long', pindex=0)

:::

<font style="color:#DF2A3F;">security</font>: 股票代码

<font style="color:#DF2A3F;">amount</font>: 交易数量（负数表示卖出）

<font style="color:#DF2A3F;">style</font>: 下单类型

<font style="color:#DF2A3F;">side</font>: short空（一般不允许）/ long多

<font style="color:#DF2A3F;">pindex</font>: 仓位号，默认为0



示例：

:::info
按限单价30买入100股

order('600000.XSHG', 100, LimitOrderStyle(30.0))

:::



#### （2）股票价值
:::info
order(security, value, style=None, side='long', pindex=0)

:::

<font style="color:#DF2A3F;">security</font>: 股票代码

<font style="color:#DF2A3F;">value</font>: 股票价值（负数表示卖出）

<font style="color:#DF2A3F;">style</font>: 下单类型

<font style="color:#DF2A3F;">side</font>: short空（一般不允许）/ long多

<font style="color:#DF2A3F;">pindex</font>: 仓位号，默认为0

示例：

:::info
按卖出价值为5000元的股票

order('600000.XSHG', -5000)

:::



#### （3）目标数量
:::info
order_target(security, amount, style=None, side='long', pindex=0, close_today=False)

:::

<font style="color:#DF2A3F;">security</font>: 股票代码

<font style="color:#DF2A3F;">amount</font>: 交易数量（负数表示卖出）

<font style="color:#DF2A3F;">style</font>: 下单类型

<font style="color:#DF2A3F;">side</font>: short空（一般不允许）/ long多

<font style="color:#DF2A3F;">pindex</font>: 仓位号，默认为0

示例：

:::info
买入平安银行所有股票到100股

order_target('000001.XSHE', 100)

:::



#### （4）成交订单
:::info
get_orders(order id=None,security=None,status=None)

:::

示例：

:::info
get_orders(order_id='123)订单id查询订单号为"123"的订单

get_orders(security='000001.XSHE') 查询所有标的为000001.XSHE的订单

:::



#### （5）未完成订单
:::info
get_open_orders()

:::

示例：

:::info
在每天交易结束之后获取当天所有的未完成订单

def after_market_close(context):

orders = get_open_orders(）

for order in orders:

log.info(_order.order_id)

:::



#### （6）撤单函数
:::info
cancel_order(order)

:::

示例：

:::info
在每天交易结束之后对未完成订单进行撤单

def after_market_close(context):

orders = get_open_orders()

for _order in orders.values():

cancel_order(order)

:::



#### （7）账号出入金
:::info
inout_cash(cash, pindex=0)

:::

<font style="color:#DF2A3F;">cash</font>: 浮点数，负数表示出金

<font style="color:#DF2A3F;">pindex</font>: 仓位号，默认为0

示例：

:::info
向账户增加10000元:

inout_cash(10000, pindex=0)

:::





### 2.代码示例
```python
def initialize(context):
    # 设定业绩标的为“沪深300”
    set_benchmark("000300.XSHG")
    g.security = '000001.XSHE'
    run_daily(market_open, time='9:30')
    run_daily(after_market_close, time='15:30')

def market_open(context):
    # 向账户增加10000元
    inout_cash(10000, pindex=0)
    # 查询可以资金
    log.info("""账户可用资金：{}""".format(context.portfolio.subportfolios[0].available_cash))
    
    # 获取账户当前现金
    cash = context.portfolio.available_cash
    
    #如果没有持仓
    if g.security not in context.portfolio.positions:
        #下单1000股
        order(g.security, 1000)
    else:
        #卖出500股
        order(g.security, -500)
        
        
def after_market_close(context):
    # 获取当天所有未完成的订单
    orders = get_open_orders()
    for _order in orders:
        log.info("""未完成订单：{}""".format(_order))
    # 对未完成订单进行撤单
    for _order in orders:
        cancel_order(_order)
```



### 小结
下单函数介绍

代码示例



## 5.<font style="color:rgb(31, 31, 31);">交易对象</font>
### 1.Order对象
Order对象： <font style="color:#DF2A3F;">订单处理流程</font>

订单创建 ->订单检查 -> 报单 -> 确认委托 -> 撮合

<font style="color:#DF2A3F;">commission</font>: 交易费用(佣金、税费等)

<font style="color:#DF2A3F;">is_buy</font>: bool值,买还是卖

<font style="color:#DF2A3F;">status</font>: 状态,一个OrderStatus值

<font style="color:#DF2A3F;">price</font>: 平均成交价格，已经成交的股票的平均成交价格



### 2.Trade对象
Trade对象：<font style="color:#DF2A3F;">订单成交</font>相关信息

<font style="color:#DF2A3F;">time</font>：交易时间，[datetime.datetime]对象

<font style="color:#DF2A3F;">security</font>：标的代码

<font style="color:#DF2A3F;">amount</font>：交易数量

<font style="color:#DF2A3F;">price</font>：交易价格

<font style="color:#DF2A3F;">trade_id</font>：交易记录id

<font style="color:#DF2A3F;">order_id</font>：对应的订单id



### 3.代码示例
```python
# 初始化函数：回测开始前只执行一次
def initialize(context):
    # 设置业绩基准：沪深300指数
    set_benchmark("000300.XSHG")
    # 指定交易股票：平安银行(000001)
    g.security = '000001.XSHE'
    
    # 每天开盘自动执行交易函数
    run_daily(market_open, time='open')
    # 每天15:30收盘后执行日志记录函数
    run_daily(after_market_close, time='15:30')

# 开盘交易逻辑：每天开盘自动运行
def market_open(context):
    # 如果没有持仓 → 买入1000股
    if g.security not in context.portfolio.positions:
        order(g.security, 1000)
    # 如果有持仓 → 卖出800股
    else:
        order(g.security, -800)

# 收盘后函数：每天15:30自动运行
def after_market_close(context):
    print("闭市后，开始查询成交记录...")
    
    # 获取当天所有成交记录（字典格式）
    trades = get_trades()
    
    # 遍历所有成交记录
    for _trade in trades.values():
        # 打印成交详情
        print("成交记录:{}".format(_trade))
        print("成交时间:{}".format(_trade.time))
        print("对应的订单id:{}".format(_trade.order_id))


"""
def market_open(context):
    #如果没有持仓
    if g.security not in context.portfolio.positions:
        orders = order(g.security, 100)
        print(orders)
        
        if orders is None:
            print("创建订单失败...")
        else:
            print('''交易费用：{}'''.format(orders.commission))
            print('''是否买单：{}'''.format(orders.is_buy))
            print('''订单状态：{}'''.format(orders.status))
            print('''订单评价成交价格：{}'''.format(orders.price))
    else:
        #卖出500股
        order(g.security, -800)
"""
```



### 4.总结
Order对象

Trade对象

代码示例



## 6.<font style="color:rgb(31, 31, 31);">策略信息</font>
### 1.Context对象
Context对象：<font style="color:#DF2A3F;">策略信息总览</font>，包含账户、时间等信息

<font style="color:#DF2A3F;">subportfolios：</font>

当前单个操作仓位的资金、标的信息，是一个SubPortfolio的数组

<font style="color:#DF2A3F;">portfolio：</font>

账户信息，即subportfolios 的汇总信息，Portfolio对象，单个操作仓位时，portfolio指向 subportfolios[0]

<font style="color:#DF2A3F;">current_dt：</font>

当前单位时间的开始时间，[datetime.datetime]对象

<font style="color:#DF2A3F;">previous date：</font>

datetime前一个交易日，[datetime.date]对象,注意，这是一个日期，是 date,而不是datetime

<font style="color:#DF2A3F;">universe：</font>

查询set_universe()设定的股票池，比如['000001.XSHE','600000.XSHG']



### 2.Position对象
Position对象：<font style="color:#DF2A3F;">输出持有的标的的信息</font>

<font style="color:#DF2A3F;">security：</font>

标的代码

<font style="color:#DF2A3F;">price：</font>

最新行情价格

<font style="color:#DF2A3F;">total_amount：</font>

总仓位，不包括挂单冻结仓位

<font style="color:#DF2A3F;">init_time：</font>

建仓时间,格式为datetime.datetime



### 3.代码示例
```python
def initialize(context):
    g.security = "000001.XSHE"
    
def handle_data(context, data):
    #如果没有持仓
    if g.security not in context.portfolio.positions:
        #下单1000股
        order(g.security, 1000)
    else:
        #卖出800股
        order(g.security, -800)
    print(type(context.portfolio.long_positions))
    long_positions_dict = context.portfolio.long_positions
    for position in list(long_positions_dict.values()):
        print(
            """"标的:{}，总仓位:{}，标的价值:{}，建仓时间:{}"""
            .format(position.security,
                position.total_amount,
                position.value,
                position.init_time)
        )
    

"""
def handle_data(context, data):
    #context.portfolio变为整数1
    context.portfolio = 1
    log.info("context.portfolio")
    log.info(context.portfolio)
    
    #恢复系统变量
    del context.portfolio
    
    #context.portfolio将变成用户账户信息
    log.info("context.portfolio.total_value")
    log.info(context.portfolio.total_value)
    
    # 输出账户总资产
    log.info("context.portfolio.total_value")
    log.info(context.portfolio.total_value)
    
    # 输出持仓金额
    log.info("context.portfolio.positions_value")
    log.info(context.portfolio.positions_value)
    
    # 输出今日日期
    log.info("context.current_dt.day")
    log.info(context.current_dt.day)
    
    # 输出总权益的累计收益
    log.info("context.portfolio.returns")
    log.info(context.portfolio.returns)
    
    # 获取仓位subportfolios[0]的可用资金
    log.info("context.subportfolios[0].available_cash")
    log.info(context.subportfolios[0].available_cash)
"""
```



### 总结
Context对象

Position对象

代码示例





## 7.<font style="color:rgb(31, 31, 31);">账户信息</font>
### 1.Portfolio对象
Portfolio对象：<font style="color:#DF2A3F;">总账户信息</font>

<font style="color:#DF2A3F;">long_positions：</font>

多单的仓位,一个dict, key是证券代码, value 是[Position]对象

<font style="color:#DF2A3F;">short_positions：</font>

空单的仓位,一个dict, key是证券代码, value 是[Position]对象

<font style="color:#DF2A3F;">total_value：</font>

总的权益，包括现金，保证金(期货)或者仓位(股票)的总价值，可用来计算收益

<font style="color:#DF2A3F;">returns：</font>

总权益的累计收益;(当前总资产+今日出入金-昨日总资产)/昨日总资产

<font style="color:#DF2A3F;">starting_cash：</font>

初始资金,现在等于inout_cash

<font style="color:#DF2A3F;">positions_value：</font>

持仓价值



### 2.SubPortfolio对象
SubPortfolio对象：<font style="color:#DF2A3F;">子账户信息</font>

<font style="color:#DF2A3F;">inout_cash：</font>

累计出入金,如初始资金1000,后来转移出去100,则这个值是1000 -100

<font style="color:#DF2A3F;">available_cash：</font>

可用资金,可用来购买证券的资金

<font style="color:#DF2A3F;">transferable_cash：</font>

可取资金，即可以提现的资金,不包括今日卖出证券所得资金

<font style="color:#DF2A3F;">locked_cash：</font>

挂单锁住资金

<font style="color:#DF2A3F;">type：</font>

账户所属类型



### 3.代码示例
```python
def initialize(context):
    g.security = "000001.XSHE"
    
def handle_data(context, data):
    #如果没有持仓
    if g.security not in context.portfolio.positions:
        #下单1000股
        order(g.security, 1000)
    else:
        #卖出800股
        order(g.security, -800)
    
    print("""累计出入金:{}""".format(context.subportfolios[0].inout_cash))
    print("""可以资金:{}""".format(context.subportfolios[0].available_cash))
    print("""可取资金:{}""".format(context.subportfolios[0].transferable_cash))
    print("""挂单锁住资金:{}""".format(context.subportfolios[0].locked_cash))
    print("""账户所属类型:{}""".format(context.subportfolios[0].type))

'''
    print("""多单的仓位:{}""".format(context.portfolio.long_positions))
    print("""空单的仓位:{}""".format(context.portfolio.short_positions))
    print("""总权益:{}""".format(context.portfolio.total_value))
    print("""总权益的累计收益率:{}""".format(context.portfolio.returns))
    print("""初始资金:{}""".format(context.portfolio.starting_cash))
    print("""持仓价值:{}""".format(context.portfolio.positions_value))
'''
```



### 小结
Portfolio对象

SubPortfolio对象

代码示例



# 八、<font style="color:rgb(31, 31, 31);">量化交易数据获取</font>
## 1.<font style="color:rgb(31, 31, 31);">获取股票财务数据</font>
### <font style="color:rgb(31, 31, 31);">1.财务数据</font>
<font style="color:rgb(31, 31, 31);">（1）查询财务数据：get_fundamentals()函数</font>

:::info
<font style="color:rgb(31, 31, 31);">get_fundamentals(query_object,date=None,statDate=None)</font>

:::

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">注意：date和statDate参数只能传入一个</font>

<font style="color:rgb(31, 31, 31);">传入date时，查询指定日期date收盘后所能看到的最近(除市值表外为最近一个季度，市值表为最近一天)的数据</font>

<font style="color:rgb(31, 31, 31);">传入statDate时，查询statDate指定的季度或者年份的财务数据</font>

<font style="color:rgb(31, 31, 31);">date/statdate: 获取一个字符串(格式类似'2015-10-15')或者datetime对象</font>

<font style="color:rgb(31, 31, 31);">query_object: 一个sqlalchemy.orm.query.Query对象,可以通过全局的query 函数获取Query对象</font>



（2）查询对象：<font style="color:rgb(31, 31, 31);">query_object</font>

<font style="color:rgb(31, 31, 31);">查询数据API,可以是</font><font style="color:#DF2A3F;">整张表，也可以是表中的多个字段或计算结果</font>

<font style="color:#DF2A3F;">filter</font><font style="color:rgb(31, 31, 31);">: 填写过滤条件，多个过滤条件可用逗号隔开，或and,or</font>

<font style="color:#DF2A3F;">order_by</font><font style="color:rgb(31, 31, 31);">: 填写排序条件</font>

<font style="color:#DF2A3F;">limit</font><font style="color:rgb(31, 31, 31);">: 限制返回的个数</font>

<font style="color:#DF2A3F;">group_by</font><font style="color:rgb(31, 31, 31);">: 分组统计</font>

<font style="color:rgb(31, 31, 31);">例如：</font>

:::info
<font style="color:rgb(31, 31, 31);">#查询 ‘000001.XSHE’的全部市值数据</font>

<font style="color:rgb(31, 31, 31);">query(valuation).filter(valuation.code=='000001.XSHE')</font>

:::

<font style="color:rgb(31, 31, 31);"></font>

<font style="color:rgb(31, 31, 31);">（3）查询多日财务数据：get_fundamentals_continuously()函数</font>

:::info
<font style="color:rgb(31, 31, 31);">get_fundamentals_ continuously(query_object, end_date=None, count=None, panel=True)</font>

:::

<font style="color:rgb(31, 31, 31);">end date: 获取一个字符串(格式类似'2015-10-15')或者datetime对象</font>

<font style="color:rgb(31, 31, 31);">count: 获取end_date前count个日期的数据，count须小于500</font>

<font style="color:rgb(31, 31, 31);">panel: 默认panel=True，返回一个pandas.Panel; 建议设置panel为False，返回等效的dataframe</font>

<font style="color:rgb(31, 31, 31);"></font>

### <font style="color:rgb(31, 31, 31);">2.代码示例</font>
```python
#查询get_fundamentals_continuously函数
q = query(
    valuation.market_cap,
    valuation.pe_ratio,
    valuation.turnover_ratio,
    indicator.eps
    ).filter(valuation.code.in_(['000001.XSHE','600000.XSHG']))

result = get_fundamentals_continuously(q,end_date='2022-01-01',count=5,panel=False)

print(result)


'''
# 查询平安银行2022年度第二季度的财务数据
query_object = query(
        income.statDate,
        income.code,
        income.basic_eps
    ).filter(
        income.code == '000001.XSHE'
        )

result = get_fundamentals(query_object, statDate='2022q2')

print(result)
'''

'''
# 查询平安银行2022年9月1日的总市值
q = query(valuation).filter(valuation.code == '000001.XSHE')

df = get_fundamentals(q, '2022-09-01')

print(df['market_cap'][0])
'''
```



### <font style="color:rgb(31, 31, 31);">小结</font>
<font style="color:rgb(31, 31, 31);">get_fundamnetals()函数</font>

<font style="color:rgb(31, 31, 31);">query_object</font>

<font style="color:rgb(31, 31, 31);">get_fundamentals_continuously()函数</font>

<font style="color:rgb(31, 31, 31);">代码示例</font>



## <font style="color:rgb(31, 31, 31);">2.获取成分股数据</font>
### 1.指数成分股
:::info
查询指定指数指定日期可交易的成分股列表

get index_stocks(index_symbol, date=None)

:::

<font style="color:#DF2A3F;">index_symbol</font>: 指数代码

<font style="color:#DF2A3F;">date/statdate</font>: 获取一个字符串(格式类似'2015-10-15)或者datetime对象

<font style="color:#DF2A3F;">返回</font>: 返回股票代码的list



### 2.行业成分股
:::info
查询指定行业的所有股票

get industy_stocks(industry_code, date=None)

:::

<font style="color:#DF2A3F;">industry_code</font>: 行业编码

<font style="color:#DF2A3F;">date/statdate</font>: 获取一个字符串(格式类似'2015-10-15’)或者datetime对象

<font style="color:#DF2A3F;">返回</font>: 返回股票代码的list



### 3.概念成分股
:::info
查询指定概念板块的所有股票

get_concept_stocks(concept_code, date=None)

:::

<font style="color:#DF2A3F;">concept_code</font>: 行业编码

<font style="color:#DF2A3F;">date/statdate</font>: 获取一个字符串(格式类似'2015-10-15)或者datetime对象

<font style="color:#DF2A3F;">返回</font>: 返回股票代码的list



### 4.代码示例
```python
# 1.指数成分股
# 返回沪深300的股票(输出100个)
index_stocks = get_index_stocks('000300.XSHG')
print(index_stocks[0:100])


# 2.行业成分股
# 获取计算机/互联网行业的成分股
industry_stocks = get_industry_stocks('I64')
print(industry_stocks)

# 3.概念成分股
# 获取风电概念板块的成分股
concept_stocks = get_concept_stocks('sc0084', date='2022-06-01')
print(concept_stocks)
```



### 小结
指数成分股

行业成分股

概念成分股

代码示例





## 3.<font style="color:rgb(31, 31, 31);">获取标的信息</font>
### 1.获取所有标的信息
:::info
获取平台支持的所有股票、基金、指数、期货、期权信息

get_all_securities(types=[], date=None)

:::

<font style="color:#DF2A3F;">types</font>: security种类,list类型。支持:'stock','fund','index','futures'等

<font style="color:#DF2A3F;">date</font>: 获取一个字符串(格式类似'2015-10-15’)或者datetime对象

<font style="color:#DF2A3F;">返回</font>: 返回dataframe对象



### 2.获取单个标的信息
:::info
获取单个标的信息，包括中文名称，简称，上市日期，退市日期，标的种类等等

get_ security_info(code,date=None)

:::

<font style="color:#DF2A3F;">code</font>: 证券代码

<font style="color:#DF2A3F;">date</font>: 获取一个字符串(格式类似'2015-10-15')或者datetime对象

<font style="color:#DF2A3F;">返回</font>: 返回数据对象



### 3.代码实战
```python
# 获取平台所有标的信息，返回前十
print(get_all_securities()[:10])

#获取平台所有ETF信息
print(get_all_securities(types=['etf'],date='2022-09-01')[:10])

# 获取平台单个标的信息
print(get_security_info('000001.XSHE'))
print(get_security_info('000001.XSHE').start_date)
print(get_security_info('000001.XSHE').type)
```



### 小结
<font style="color:rgb(31, 31, 31);">获取所有标的信息</font>

<font style="color:rgb(31, 31, 31);">获取单个标的信息</font>

<font style="color:rgb(31, 31, 31);">代码实战</font>

<font style="color:rgb(31, 31, 31);"></font>

## <font style="color:rgb(31, 31, 31);">4.获取股票交易数据</font>
### 1.获取行情数据
:::info
获取证券行情数据，可查询多个标的多个数据字段

get_price(security, 

start_date=None, 

end_date=None, 

frequency='daily',

fields=None, 

skip_paused=False, 

fq='pre', 

count=None, 

panel=True,

fill_paused=True)

:::

<font style="color:#DF2A3F;">security</font>: 

一支股票代码或者一个股票代码的list

<font style="color:#DF2A3F;">count</font>:

与start_date二选一，不可同时使用。数量，返回的结果集的行数，即表示获取

end_date 之前几个frequency的数据

<font style="color:#DF2A3F;">start_date</font>:

与count二选一，不可同时使用。字符串或者datetime对象,开始时间

<font style="color:#DF2A3F;">end_date</font>:

同start_date,结束时间

<font style="color:#DF2A3F;">frequence</font>:

单位时间长度，几天或者几分钟，现在支持'Xd,'Xm',‘daily(等同于'1d),

<font style="color:#DF2A3F;">fields:</font>

字符串list,选择要获取的行情数据字段，默认是None(常用['open','close','high'，'low','volume','money']这几个标准字段)

<font style="color:#DF2A3F;">skip_paused</font>:

是否跳过不交易日期(包括停牌，未上市或者退市后的日期

<font style="color:#DF2A3F;">fq</font>:

复权选项(对股票/基金的价格字段、成交量字段及factor字段生效)

<font style="color:#DF2A3F;">panel</font>:

获取多标的数据时建议设置panel为False,在pandas 0.25版后，panel被彻底移除

<font style="color:#DF2A3F;">fill_paused</font>:

对于停牌股票的价格处理，默认为True;True表示用preclose价格填充;





### 2.获取龙虎榜数据
:::info
获取龙虎榜数据

get_billboard_list(stock_list, start_date, end_date, count)

:::

<font style="color:#DF2A3F;">stock_list</font>: 包含股票代码的list，当值为None时，返回指定日期的所有股票

<font style="color:#DF2A3F;">start_date</font>: 开始日期

<font style="color:#DF2A3F;">end_date</font>: 结束日期

<font style="color:#DF2A3F;">count</font>: 交易日数量，可以与end_date同时使用，表示获取end_date前count 个交易日的数据(含end_date当日)



### 3.代码实战
```python
# 获取一只股票
# 获取000001.XSHE的股票数据
df = get_price(
        security='000001.XSHE',
        start_date = '2015-01-01',
        end_date = '2015-01-31 23:00:00',
        frequency = '1m',
        fields = ['open','close']
    
    )
print(df)


#获取多只股票
#获取中证100所有成分股的股票数据
df = get_price(get_index_stocks('000903.XSHG'),panel = False)
# 只打印第一行的数据
print(df[0:1])
# 只打印平安银行的数据
print (df.loc[df['code']=='000001.XsHE'])


#获取龙虎榜数据
#获取2022-09-01前2个交易日的龙虎榜数据
df = get_billboard_list(stock_list=None,end_date='2022-09-01',count=2)
print(df)

print(df[['code','abnormal_name','sales_depart_name','rank']][:10])

```



### 小结
获取行情数据

获取龙虎榜数据

代码示例



# 九、量化选股
## 1.量化选股概况
### 1.量化选股概况
**量化选股**

:::info
利用数量化的方法选择股票组合，期望该股票组合能够获得超越基准收益率的投资行为

:::



**技术面选股**

:::info
利用各种技术理论或技术指标来分析和预测股票的未来价格趋势

:::



**基本面选股**

:::info
通过对一家上市公司在发展过程中面临的外部因素和自身因素进行分析，对其未来的发展前景进行预测，判断该上市公司的股票是否值得买进

:::



### 2.量化选股注意事项
:::info
分配多股，减少单股重仓的情况（我们选出的是股票的组合）

全面研究个股基本面，增强个股判断逻辑和支撑

主动投资而非被动投资

只是提高胜率的工具之一

:::



### 3.代码示例
```python
'''
白马股选股策略 极简易懂版
选股5条件：
1. 总市值 > 50亿
2. 上市满750天，剔除次新股
3. 流通比例 > 95% 全流通
4. 销售毛利率 > 20%
5. ROE > 20%

规则：按市值从大到小排序，持有前20只，每100个交易日调仓
'''
import datetime
from datetime import timedelta

# 初始化：策略启动只跑一次
def initialize(context):
    set_benchmark('000300.XSHG')      # 对标沪深300
    set_option('use_real_price', True) # 动态复权
    set_option('order_volume_ratio', 1)

    # 交易手续费设置
    cost = OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.003,
        close_commission=0.003,
        close_today_commission=0,
        min_commission=5
    )
    set_order_cost(cost, type='stock')

    # 全局参数
    g.stock_num = 20       # 持仓20只
    g.day_count = 0        # 交易日计数
    g.turn_cycle = 100     # 每100天调仓

    run_daily(trade, 'every_bar')

# 核心选股：严格对应5条条件
def get_white_horse_stocks(context):
    # 构造查询字段 + 过滤条件
    q = query(
        indicator.code,
        valuation.market_cap,               # 总市值(亿元)
        valuation.circulating_market_cap,   # 流通市值(亿元)
        indicator.gross_profit_margin,      # 销售毛利率
        indicator.roe                       # 净资产收益率ROE
    ).filter(
        valuation.market_cap > 50,                                   # 条件1：总市值>50亿
        valuation.circulating_market_cap > valuation.market_cap*0.95,# 条件2：流通比例>95%
        indicator.gross_profit_margin > 20,                          # 条件3：毛利率>20%
        indicator.roe > 20                                          # 条件4：ROE>20%
    ).order_by(valuation.market_cap.desc()).limit(100)  # 市值从大到小

    # 获取选股结果
    df = get_fundamentals(q)
    stock_list = list(df['code'])

    # 条件5：剔除上市不足750天次新股
    stock_list = filter_new_stock(stock_list, context.current_dt, 750)
    # 剔除停牌股
    stock_list = filter_paused_stock(stock_list)
    # 只取前20只
    return stock_list[:20]

# 过滤停牌股票
def filter_paused_stock(stock_list):
    current_data = get_current_data()
    return [s for s in stock_list if not current_data[s].paused]

# 剔除次新股：上市不满指定天数不要
def filter_new_stock(stock_list, now_date, need_days):
    res = []
    for stock in stock_list:
        # 获取上市日期
        list_date = get_security_info(stock).start_date
        # 计算界限日期：当前日期往前推need_days天
        limit_date = (now_date - timedelta(days=need_days)).date()
        # 上市早于界限日期 = 满足上市天数要求
        if list_date < limit_date:
            res.append(stock)
    return res

# 交易主函数
def trade(context):
    # 到达调仓周期，执行换股
    if g.day_count % g.turn_cycle == 0:
        # 选出最新白马股列表
        target_stocks = get_white_horse_stocks(context)
        # 当前持仓
        hold_stocks = list(context.portfolio.positions.keys())

        # 卖出：不在新名单里的老股票
        for s in hold_stocks:
            if s not in target_stocks:
                order_target_value(s, 0)

        # 剩余资金平均分配
        cash_per_stock = context.portfolio.available_cash / g.stock_num

        # 买入新入选股票
        for s in target_stocks:
            if s not in context.portfolio.positions:
                order_value(s, cash_per_stock)

        # 重置计数
        g.day_count = 1
    else:
        # 非调仓日，计数+1
        g.day_count += 1
```



### 总结
基本面量化选股概况

量化选股注意事项

代码示例



## 2.营收因子选股
### 1.财务因子介绍
**财务因子：**

评价企业的基本面情况，通常包括<font style="color:#DF2A3F;">成长类因子</font>，<font style="color:#DF2A3F;">规模类因子</font>，<font style="color:#DF2A3F;">价值类因子</font>以及<font style="color:#DF2A3F;">质量类因子</font>

**成长类因子：**

在财务因子选股中，常用的方法是选用成长类因子进行选股。成长类因子包括<font style="color:#DF2A3F;">营收因子</font>与<font style="color:#DF2A3F;">利润因子</font>

**规模类因子：**

规模类因子反映公司规模情况，主要用于体现市值大小对投资收益的影响。

规模类因子包括<font style="color:#DF2A3F;">总市值</font>，<font style="color:#DF2A3F;">流通市值</font>，<font style="color:#DF2A3F;">总股本</font>，<font style="color:#DF2A3F;">流通股本</font>

**价值类因子：**

价值投资是一个久经考验的投资策略，惯例是购买那种相对低价的股票，转换成在基本面标准度量股息账面价值、利润、现金流或其他公司价值的方法。值类因子包括<font style="color:#DF2A3F;">市净率</font>，<font style="color:#DF2A3F;">市销率</font>，以及<font style="color:#DF2A3F;">市盈率</font>

**<font style="color:#000000;">质量类因子：</font>**

质量类因子指与股票的财务质量、资本结构相关的因子。质量类因子包括<font style="color:#DF2A3F;">净资产收益率</font>，以及<font style="color:#DF2A3F;">总资产净利率</font>



### 2.营收因子与利润因子
**营收因子：**

营收因子包括<font style="color:#DF2A3F;">营业收入同比增长率</font>、<font style="color:#DF2A3F;">营业收入环比增长率</font>、<font style="color:#DF2A3F;">营业总收入</font>

**利润因子：**

利润因子包括<font style="color:#DF2A3F;">净利润同比增长率</font>、<font style="color:#DF2A3F;">净利润环比增长率</font>、<font style="color:#DF2A3F;">营业利润率</font>、<font style="color:#DF2A3F;">销售净利润</font>、<font style="color:#DF2A3F;">销售毛利率</font>



### 3.营收因子详述
**营收因子同比增长率：**

:::info
(当期营业收入-上期营业收入) / 上期营业收入 * 100%

上期营业收入一般指上一年度/季度/月度同期营业收，此处指上一年度的同期营业收入。

get_fundamentals(

query(indicator.inc revenue year_on_year).filter(查询条件}),

date={查询日期}

)

:::

**营收因子环比增长率：**

:::info
(本期营业收入的值-上一期营业收入的值)/上一期营业收入的值 * 100%

环比增长率是针对上一期的，而同比增长率是相对于上一年度同一期的

get_fundamentals(

query(indicator.inc_revenue_annual).filter({查询条件}),

date={查询日期}

)

:::

**营业总收入：**

:::info
主营业务收入+其他业务收入

net_profit to_total_revenue

get_fundamentals(

query(indicator.net_profit_to_total_revenue).filter({查询条件}),

date={查询日期)

)

:::



### 小结
财务类因子

营收因子与利润因子

营收因子详述

代码示例



## 3.利润因子
### 1.净利润同比增长率
:::info
净利润指企业的税后利润

<font style="color:#DF2A3F;">(当期净利润-上期净利润)/上期净利润绝对值*100%</font>

上期净利润指上一年度的同期净利润



get_fundamentals(

query(indicator.inc_net_profit_year_on_year).filter({查询条件}),

date={查询日期)

)

:::



### 2.净利润环比增长率
:::info
<font style="color:#DF2A3F;">(本期净利润-上一期净利润)/上一期净利润*100%</font>

环比增长率是针对上一期的，而同比增长率是相对子上一年度同一期的



get_fundamentals(

query(indicator.inc_net_profit_annual).filter({查询条件}),

date={查询日期)

)

:::



### 3.营业利润率
:::info
指经营所得的营业利润占销售净额的百分比，或占投入资本额的百分比

<font style="color:#DF2A3F;">营业利润/全部业务收入*100%</font>



get_fundamentals(

query(indicator.operation_profit_to_total_revenue).filter({查询条件}),

date={查询日期)

)

:::



### 4.销售净利润
:::info
指企业实现净利润与销售收入的对比关系，用以衡量企业在一定时期的销售收入获取的能力

<font style="color:#DF2A3F;">净利润/销售收入*100%</font>



get_fundamentals(

query(indicator.net_profit_margin).filter({查询条件}),

date={查询日期)

)

:::



### 5.销售毛利润
:::info
<font style="color:#DF2A3F;">净利润扣税，毛利润不扣税</font>

毛利是销售净收入与产品成本的差销售毛利率是毛利占销售净值的百分比

<font style="color:#DF2A3F;">(销售净收入-产品成本)/销售净收入</font>



get_fundamentals(

query(indicator.gross_profit_margin).filter({查询条件}),

date={查询日期)

)

:::



### 6.代码示例
```python
print("--净利润同比增长率大于300的股票代码----------------------------------------------")
# 净利润同比增长率大于300的股票代码
query_object = query(
        indicator.code,
        indicator.inc_net_profit_year_on_year
    ).filter(
        indicator.inc_net_profit_year_on_year > 300    
    ).order_by(
        indicator.inc_net_profit_year_on_year.desc()
    )
df = get_fundamentals(query_object, date='2022-09-01')
print(df)


print("--净利润环比增长率大于500的股票代码----------------------------------------------")
# 净利润环比增长率大于500的股票代码
query_object = query(
        indicator.code,
        indicator.inc_net_profit_annual
    ).filter(
        indicator.inc_net_profit_annual > 500    
    ).order_by(
        indicator.inc_net_profit_annual.desc()
    )
df = get_fundamentals(query_object, date='2022-09-01')
print(df)

print("--营业利润率大于200的股票代码----------------------------------------------")
# 营业利润率大于200的股票代码
query_object = query(
        indicator.code,
        indicator.operation_profit_to_total_revenue
    ).filter(
        indicator.operation_profit_to_total_revenue > 200    
    ).order_by(
        indicator.operation_profit_to_total_revenue.desc()
    )
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])


print("--营业净利润率最高的5只股票代码----------------------------------------------")
# 营业净利润率最高的5只股票代码
query_object = query(
        indicator.code,
        indicator.net_profit_margin
    ).order_by(
        indicator.net_profit_margin.desc()
    )
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])

print("--销售毛利润最高的5只股票代码----------------------------------------------")
# 营业净利润率大于200的股票代码
query_object = query(
        indicator.code,
        indicator.gross_profit_margin
    ).order_by(
        indicator.gross_profit_margin.desc()
    )
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])
```



### 小结
净利润同比增长率

净利润环比增长率

营业利润率

销售净利润

销售毛利润

代码示例



## 4.规模类因子
### 1.规模类因子介绍
:::info
**规模类因子：**

规模类因子反映公司规模情况,主要用于体现市值大小对投资收益的影响

**指标：**

规模类因子包括总市值、流通市值、总股本、流通股本

:::



### 2.总市值
:::info
在某特定时间内股票总价值

<font style="color:#DF2A3F;">总股本数*股价</font>

总市值用来表示个股权重大小或大盘的规模大小



get_fundamentals(

query(valuation.market_cap).filter({查询条件}),

date={查询日期)

)

:::



### 3.流通市值
:::info
在某特定时间内当时可交易流通股票总价值

<font style="color:#DF2A3F;">可交易的流通股股数*股价</font>

<font style="color:#DF2A3F;">流通市值占</font>总市值的<font style="color:#DF2A3F;">比</font>重(流通盘比例)<font style="color:#DF2A3F;">越大</font>，说明股票的市场价格<font style="color:#DF2A3F;">越</font>能反应出公司的<font style="color:#DF2A3F;">真实</font>价值



get_fundamentals(

query(valuation.market_cap).filter({查询条件}),

date={查询日期)

)

:::



### 4.总股本
:::info
指公司已发行的普通股股份总数(包含A股、B股和H股的总股本)，单位万股

A股：普通人可以买到的股票

B股：非人民币结算，一般是美元

H股：港股



get_fundamentals(

query(valuation.capitalization).filter({查询条件}),

date={查询日期)

)

:::



### 5.流通股本
:::info
指公司已发行的境内上市流通、以人民币兑换的股份总数，即A股市场的流通股本，单位万股



get_fundamentals(

query(valuation.circulating_cap).filter({查询条件}),

date={查询日期)

)

:::



### 6.代码示例
```python

```





### 小结
规模类因子介绍

总市值

流通市值

总股本

流通股本

代码示例



## 5.价值类因子
### 1.价值类因子介绍
:::info
**价值类因子：**

即<font style="color:#DF2A3F;">价值投资</font>，是一种久经考验的<font style="color:#DF2A3F;">投资策略</font>。

通过购买那种<font style="color:#DF2A3F;">相对低价</font>的股票，转换成在基本面标准度量<font style="color:#DF2A3F;">股息</font>、<font style="color:#DF2A3F;">账面价值</font>、<font style="color:#DF2A3F;">利润</font>、<font style="color:#DF2A3F;">现金流或其他公司价值</font>的方法

**指标：**

价值类因子包括<font style="color:#DF2A3F;">市净率</font>、<font style="color:#DF2A3F;">市销率</font>、<font style="color:#DF2A3F;">(动态/静态)市盈率</font>

:::



### 2.市净率**（PB）**
:::info
<font style="color:#DF2A3F;">每股市价/每股净资产</font>

市净率可用于股票投资分析，一般来说市净率较低的股票，投资价值较高。相反，则投资价值较低。

在判断投资价值时还要考虑当时的市场环境以及公司经营情况、赢利能力等因素



get_fundamentals(

query(valuation.pb_ratio).filter({查询条件}),

date={查询日期}

)

:::



### 3.市销率（PS）
:::info
<font style="color:#DF2A3F;">股价/每股销售额</font>

在国内证券市场，运用这一指标来选股可以剔除那些市盈率很低但主营业务没有核心竞争力而主要是依靠非经营性损益而增加利润的股票(上市公司)。该项指标既有助于考察公司收益基础的稳定性和可靠性，又能有效把握其收益的质量水平



get_fundamentals(

query(valuation.ps_ratio).filter({查询条件}),

date={查询日期}

)

:::



### 4.（动态/静态）市盈率
:::info
**动态市盈率：**

动态市盈率是指还没有真正实现的下一年度的预测利润的市盈率

<font style="color:#DF2A3F;">动态市盈率=股票现价/未来每股收益的预测值</font>



**静态市盈率：**

静态市盈率(即广泛意义上的市盈率)表示该公司需要累积多少年的盈利才能达到如今的市价水平

<font style="color:#DF2A3F;">静态市盈率=股票现价/每股收益</font>



<font style="color:#DF2A3F;">市盈率指标数值越小说明投资回收期越短，风险越小</font>



get_fundamentals(

query(valuation.pcf_ratio, valuation.pe_ratio).filter({查询条件}),

date={查询日期}

)

:::



### 5.代码示例
```python
print("--市净率小于1.5，总市值大于8000亿的股票代码----------------------------------------------")
# 市净率小于1.5，总市值大于8000亿的股票代码
query_object = query(
        valuation.code,
        valuation.pb_ratio,
        valuation.market_cap
    ).filter(
        valuation.market_cap > 8000,
        valuation.pb_ratio < 1.5
    ).order_by(
        valuation.pb_ratio.desc()
    )
    
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])


print("--市净率小于1.5，市销率小于0.5的股票代码----------------------------------------------")
# 市净率小于1.5，总市值大于8000亿的股票代码
query_object = query(
        valuation.code,
        valuation.pb_ratio,
        valuation.ps_ratio
    ).filter(
        valuation.ps_ratio < 0.5,
        valuation.pb_ratio < 1.5
    ).order_by(
        valuation.pb_ratio.asc()
    )
    
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])

print("--动态市盈率小于6,市销率小于0.5,静态市盈率在3-5的股票代码,按静态市盈率排序--")
# 动态市盈率小于6,市销率小于0.5,静态市盈率在3-5的股票代码,按静态市盈率排序
query_object = query(
        valuation.code,
        valuation.pcf_ratio,
        valuation.pe_ratio,
        valuation.ps_ratio
    ).filter(
        valuation.ps_ratio < 0.5,
        valuation.pcf_ratio < 6,
        valuation.pe_ratio > 3,
        valuation.pe_ratio < 5
    ).order_by(
        valuation.pe_ratio.asc()
    )
    
df = get_fundamentals(query_object, date='2022-09-01')
print(df[:5])
```



### 小结
价值类因子介绍

市净率(PB)

市销率(PS)

(动态/静态)市盈率



## 6.质量类因子
### 1.质量类因子介绍
:::info
**质量类因子介绍：**

质量类因子指与股票的财务质量、资本结构相关的因子。影响质量因子的因素大致包括:公司的盈利能力、盈利稳定性、资本结构成长性、会计质量、派息/摊薄、投资能力等



**指标：**

质量类因子包括<font style="color:#DF2A3F;">净资产收益率</font>、<font style="color:#DF2A3F;">总资产净利率</font>

:::



### 2.净资产收益率
:::info
<font style="color:#DF2A3F;">税后利润/所有者权益（净资产）x100%</font>

净资产收益率是企业税后利润除以净资产得到的百分比率，该指际反映股东权益的收益水平，用以衡量企业运用自有资本的效率。<font style="color:#DF2A3F;">指标值越高，说明投资带来的收益越高</font>



get_fundamentals(

query(indicator.roe).filter({查询条件}),

date={查询日期}

)

:::



### 3.总资产净利率
:::info
<font style="color:#DF2A3F;">净利润/平均资产总额x100%</font>

总资产净利率反映的是公司运用全部资产所获得利润的水平，

即公司每占(用1元的资产平均能获得多少元的利润。

<font style="color:#DF2A3F;">总资产净利率越高</font>，表明公司投:入产出水平越高，资产运营越有效，成本费用的控制水平越高



get_fundamentals(

query(indicator.roa).filter({查询条件}),

date={查询日期}

)

:::



### 4.代码示例
```python
print("--净资产收益率大于50的股票代码,降序排列----------------------------------------------")
# 净资产收益率大于50的的股票代码,降序排列
query_object = query(
        indicator.code,
        indicator.roe
    ).filter(
        indicator.roe > 50
    ).order_by(
        indicator.roe.desc()
    )
    
df = get_fundamentals(query_object, date='2026-01-01')
print(df[:10])


print("--总资产净利率大于10的股票代码,降序排列----------------------------------------------")
# 总资产净利率大于10的的股票代码,降序排列
query_object = query(
        indicator.code,
        indicator.roa
    ).filter(
        indicator.roa > 10
    ).order_by(
        indicator.roa.desc()
    )
    
df = get_fundamentals(query_object, date='2026-01-01')
print(df[:10])





```



### 总结
质量类因子介绍

净资产收益率（越高越好）

总资产净利率（越高越好）

代码示例



# 十、量化择时
## 1.量化择时
### 1.量化择时基本概念
:::info
**量化择时：**

量化择时就是利用数量化的方法，通过对各种宏观微观指标的量化分析，试图找到影响大盘走势的关键信息，并且对未来走势进行预测。通俗来说，就是采甩<font style="color:#DF2A3F;">量化的方式判断买点和卖点</font>

**常用方法：**

常用的量化择时方法有<font style="color:#DF2A3F;">趋势量化择时</font>、<font style="color:#DF2A3F;">市场情绪量化择时</font>

:::



### 2.量化择时常用方法
:::info
**趋势择时：**

基本思想来自于<font style="color:#DF2A3F;">技术分析</font>，技术分析认为<font style="color:#DF2A3F;">趋势存在延续性</font>，因此只要找到趋势方向，跟随操作即可。趋势择时的主要指标有<font style="color:#DF2A3F;">MA、MACD、DMA</font>等

**市场情绪择时：**

利用投资者的热情程度来判断大势方向，当情绪热烈时，大盘可能会继续涨；当投资者情绪低迷，大盘可能继续下跌。常用方法：<font style="color:#DF2A3F;">调查问卷</font>、<font style="color:#DF2A3F;">开户人数</font>、<font style="color:#DF2A3F;">搜索指数</font>、<font style="color:#DF2A3F;">报告评级</font>、<font style="color:#DF2A3F;">融资融券数据</font>、<font style="color:#DF2A3F;">舆情数据</font>等

:::



### 3.技术指标理论
:::info
**三个假设：**

技术指标的理论基础基于三项市场假设：<font style="color:#DF2A3F;">市场行为涵盖一切信息</font>、<font style="color:#DF2A3F;">价格沿趋势移动</font>、<font style="color:#DF2A3F;">历史会重演</font>

**技术指标：**

技术指标是技术分析中使用最多的一种方法，通过考虑<font style="color:#DF2A3F;">市场行为的多个方面</font>建立一个<font style="color:#DF2A3F;">数学模型</font>，并给出完整的<font style="color:#DF2A3F;">数学计算公式</font>，从而得到一个体现证券市场的某个方面内在实质的数字，即所谓的<font style="color:#DF2A3F;">技术指标值</font>

:::



### 4.技术指标分类
:::info
**趋向指标：**

技术趋向指标是识别和追踪有趋势的图形类指标,其特点是<font style="color:#DF2A3F;">不试图捕顶和测底</font>，如<font style="color:#DF2A3F;">均线指标</font>、<font style="color:#DF2A3F;">MACD指标</font>等

**反趋向指标：**

反趋向指标又称为<font style="color:#DF2A3F;">振荡指标</font>，是识别和追踪趋势运行的转折点的图形类指标，其特点是<font style="color:#DF2A3F;">具有强烈的捕顶和捉底的意图</font>，对市场转折点较敏感,如<font style="color:#DF2A3F;">随机指标KDJ、强弱指标RSI</font>等

**压力支撑指标：**

压力支撑指标，又称通道指标，是通过顶部轨道线和底部轨道线,试图捕捉行情的顶部和底部的图形类指标，其特点是<font style="color:#DF2A3F;">具有明显的压力线</font>,也有<font style="color:#DF2A3F;">明显的支撑线</font>,如<font style="color:#DF2A3F;">布林带BOLL指标</font>、<font style="color:#DF2A3F;">XS薛斯通道指标</font>

**<font style="color:#000000;">量价指标：</font>**

<font style="color:#000000;">量价指标就是通过成交量变动来分析捕捉价格未来走势的图形类指标,其特点是</font><font style="color:#DF2A3F;">分析成交量与价格涨跌的关系</font><font style="color:#000000;">，如</font><font style="color:#DF2A3F;">OBV能量潮指标</font><font style="color:#000000;">、</font><font style="color:#DF2A3F;">VOL成交量指标</font><font style="color:#000000;">等</font>

:::



### 小结
量化择时基本概念（通过量化找到买点和卖点）

量化择时分类（趋势择时、市场情绪择时）

技术指标理论

技术指标分类



## 2.趋向指标（上）
### 1.趋向指标介绍
:::info
**定义：**

趋向指标(DMI)又称动向指标。其基本原理是通过分析股价在上升及下跌过程中的<font style="color:#DF2A3F;">均衡</font>，即<font style="color:#DF2A3F;">供需关系受价格</font>的变动由<font style="color:#DF2A3F;">均衡到失衡</font>的循环过程，从而提供对<font style="color:#DF2A3F;">趋势判断</font>的依据

**原理：**

在大多数指标中都是以每一日的收盘价走势及升幅、跌幅的累计数来计算出不同的分析数据,其不足之处在于<font style="color:#DF2A3F;">忽略了每一日的高价低价的波动幅度</font>。而DMI指标则是把<font style="color:#DF2A3F;">每日的高低波动的幅度因素</font>计算在内,来分析预测未来的走势

:::



### 2.MACD
:::info
即平滑异同移动平均线，是由美国投资家杰拉尔德·阿佩尔在20世纪70年代末提出的，主要表示经过平滑处理后均线的差异程度。一般用来研判<font style="color:#DF2A3F;">股票价格变化的方向</font>、<font style="color:#DF2A3F;">强度和趋势</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778654598194-2b387b26-da01-4a01-8541-5e6a44da78b0.png" width="1023" title="" crop="0,0,1,1" id="ud073ef45" class="ne-image">

快线DIFF上穿慢线DEA，<font style="color:#DF2A3F;">红柱出现的第一天</font>，称为<font style="color:#DF2A3F;">金叉</font>，是<font style="color:#DF2A3F;">买进持有</font>的时机

快线DIFF下穿慢线DEA，<font style="color:#DF2A3F;">绿柱出现的第一天</font>，称为<font style="color:#DF2A3F;">死叉</font>，是<font style="color:#DF2A3F;">卖出空仓</font>的时机



:::info
实现方式：

from jqlib.technical_analysis import *

MACD(security_list, check_date, SHORT, LONG, MID)

:::

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">SHORT</font>: 快线[短周期均线]

<font style="color:#DF2A3F;">LONG</font>: 慢线[长周期均线】

<font style="color:#DF2A3F;">MID</font>: 计算signalperiod天的macd的EMA均线

:::info
示例

MACD(security_list='000001.XSHE',check_date='2022-09-01',SHORT=12,LONG=26,MID=9)

返回

DIF,DEA和MACD的值

字典(dict): 键(key)为股票代码，值(value)为数据

:::



### 3.EMV
:::info
即简易波动指标。<font style="color:#DF2A3F;">股票中间价</font>的<font style="color:#DF2A3F;">相对波动幅度</font>是以<font style="color:#DF2A3F;">相对成交除以相对振幅</font>作为衡量<font style="color:#DF2A3F;">股票中间价波动百分比</font>的基数。<font style="color:#DF2A3F;">EMV值增加</font>代表<font style="color:#DF2A3F;">成交量增加</font>，这是<font style="color:#DF2A3F;">价格上升</font>阶段的正常信号。<font style="color:#DF2A3F;">EMV下跌</font>代表了<font style="color:#DF2A3F;">缩量下降</font>，这也是<font style="color:#DF2A3F;">价格下跌</font>阶段的正常信号



1.A=(今日最高+今日最低)/2

B=(前日最高+前日最低)/2

C=今日最高-今日最低

2.EM=(A-B)*C/今日成交额

3.EMV=N日内EM的累和

4.MAEMV=EMV的M日的简单移动平均

5.参数N为14，参数M为9

:::



<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778655073149-7e45b31e-b4bf-46cb-bc63-dd9baebbfe08.png" width="395" title="" crop="0,0,1,1" id="u592d266b" class="ne-image">

当EMV从底部到顶部穿过0轴时，<font style="color:#DF2A3F;">买入</font>

当EMV从上到下穿过0轴时，<font style="color:#DF2A3F;">卖出</font>



:::info
代码：

from jqlib.technical analysis import *

EMV(security_list, check_date, N, M, unit = '1d', include_now = True, fq_ref_date = None)

:::

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">N</font>: N日内EM累加和

<font style="color:#DF2A3F;">M</font>: MAEMV(即EMV的M日简单移动平均)

常见的参数N为14，参数M为9

<font style="color:#DF2A3F;">unit</font>: 统计周期，默认为'1d'

<font style="color:#DF2A3F;">include_now</font>: 是否包含当前周期，默认为True

<font style="color:#DF2A3F;">fq_ref_date</font>: 复权基准日，默认为None

:::info
示例

EMV(security_list, check_date=' 2022-09-01' , N= 14, M =9, unit = '1d', 

include_now =True,fq_ref_date = None)

返回

EMV和MAEMV的值

字典(dict): 键(key)为股票代码，值(value)为数据

:::



### 4.UOS
:::info
即终极波动指标。UOS指标是一种多方位功能的指标，除了趋势确认及超买超卖方面的作用之外，它的“突破”讯号不仅可以提供最适当的交易时机之外，更可以进一步加强指标的可靠度



1.TH=今日最高价和昨日收盘价的较大值

2.TL=今日最低价和昨日收盘价的较小值

3.ACC1=(收盘价-TL)的N1日累和/(TH-TL的N1日累和)

ACC2=(收盘价-TL)的N2日累和/(TH-TL的N2日累和)

ACC3=(收盘价-TL)的N3日累和/(TH-TL的N3日累和)

4.UOS=(ACC1*N2*N3+ACC2*N1*N3+ACC3*N1*N2)*100/(N1*N2+N1*N3+N2*N3)

5.MAUOS=UOS的M日指数平滑移动平均

6.参数N1=7,N2=14,N3=28,M=6



UOS短线抄底：**<font style="color:#DF2A3F;">UOS上穿50</font>**

UOS短线卖顶：**<font style="color:#DF2A3F;">UOS下穿65</font>**

UOS中长期抄底：**<font style="color:#DF2A3F;">UOS上穿35</font>**

UOS中长期卖顶：**<font style="color:#DF2A3F;">UOS下穿70</font>**

:::



:::info
from jqlib.technical analysis import *

UOS(security_list, check_date, N1 = 7, N2 = 14, N3 = 28, M= 6, unit = '1d', include_ now = True, fq_ref_ date = None)

security_list:股票列表

check_date:要查询数据的日期

N1: 统计的天数N1

N2: 统计的天数N2

N3: 统计的天数N3

M: 统计天数M

unit: 统计周期，默认为'1d'

include_now: 是否包含当前周期，默认为True

fq_ref _date: 复权基准日，默认为None



示例

UOS(security,check_date='2022-09-01',N1=7,N2=14,N3=28,M=6)

返回

终极指标和MAUOS的值

字典(dict):键(key)为股票代码，值(value)为数据

:::



### 5.代码示例
```python

from jqlib.technical_analysis import *

#获得MACD
print("--MACD---------------------------------------------------------")
security = '000001.XSHE'
DIF,DEA,_MACD = MACD(
    security_list=security,
    check_date='2022-09-01',
    SHORT=12,
    LONG=26,
    MID=9
)
print(DIF)
print(DEA)
print(_MACD)

# 获得多只股票的EMV
print("--EMV---------------------------------------------------------")
security_list = ['000001.XSHE','000002.XSHE','601211.XSHG']
EMV, MAEMV = EMV(
    security_list=security_list,
    check_date='2022-09-01',
    N=14,
    M=9
)
print(EMV)
print(MAEMV)

# 获得单只股票的UOS
print("--UOS---------------------------------------------------------")
security_list = ['000001.XSHE']
UOS, MAUOS = UOS(
    security_list=security_list,
    check_date='2022-09-01',
    N1=7,
    N2=14,
    N3=28,
    M=6
)
print(UOS)
print(MAUOS)
```



### 小结
趋向指标介绍

MACD （股价变化的方向、强度、趋势；金叉和死叉的判断）

EMV （简易波动指标，股票中间价带来的相对振幅）

UOS （终极波动指标）

代码示例



## 3.趋向指标（中）
### 1.GDX 鬼道线
:::info
即鬼道线，它反应的是中心线于收盘价的乖离，对趋势线做了平滑和修正处理，更精确的反应了股价运行规律

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778659058095-7338f184-f9c0-43a0-ba04-c686b31df45b.png" width="550" title="" crop="0,0,1,1" id="ua3578415" class="ne-image">

AA赋值: (2*收盘价+最高价+最低价)4-收盘价的N日简单移动平均的绝对值/收盘价的N日简单移动平均

输出济安线: 以AA为权重收盘价的动态移动平均

输出压力线: (1+M/100)*JAX

输出支撑线: (1-M/100)*JAX



**当股价上升到压力线时，****<font style="color:#DF2A3F;">卖出</font>**

**当股价下跌到支撑线时，****<font style="color:#DF2A3F;">买进</font>**



### 2.JS 加速线
:::info
即加速线，通过当前股价与一段时间以前的股价相对比来测量股价涨跌的速度来确定其运行的快慢的指标



JS指标包含四条曲线，分别是JS以及三条JS不同周期的简单移动平均线，一般情况下，分别取值5日、10日、20日的简单移动平均。具体的计算公式如下:

JS=100*(收盘价-N日前的收盘价)/(N*N日前的收盘价);

MAJS1=JS的5日简单移动平均;

MAJS2=JS的10日简单移动平均;

MAJS3=JS的20日简单移动平均;

这里的N日，一般取值为5日。



**当JS线向下交叉JSMA线，****<font style="color:#DF2A3F;">卖出</font>**

**当JS线向上交叉JSMA线，****<font style="color:#DF2A3F;">买进</font>**

:::



实现方式：

:::info
from jqlib.technical analysis import *

JS(security_list, check date, N = 5, M1 = 5, M2 = 10, M3 = 20, unit = '1d', include now = True, fq_ref date = None)

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">N</font>: 统计的天数N

<font style="color:#DF2A3F;">M1</font>: 统计的天数M1

<font style="color:#DF2A3F;">M2</font>: 统计的天数M2

<font style="color:#DF2A3F;">M3</font>: 统计的天数M3



示例

JS(security, check_date='2022-09-01', N=5, M1=5, M2=10, M3=20)

返回

JS、 MAJS1、 MAJS2和MAJS3

:::



### 3.代码示例
```python
from jqlib.technical_analysis import * 


#获得多只股票的GDX指标
print("--获得多只股票的GDX指标------------------------------------")
security_list = ['000001.XSHE','000002.XSHE','601211.XSHG']
JAX,YLX,ZCX = GDX(security_list,check_date='2022-09-01',N=14,M=9)
for stock in security_list:
    print(stock)
    print('济安线的值为: {}'.format(JAX[stock]))
    print('压力线的值为: {}'.format(YLX[stock]))
    print('支撑线的值为: {}'.format(ZCX[stock]))
    
    
#获得单只股票的JS指标
print("--获得单只股票的JS指标------------------------------------")
security = '000001.XSHE'
_JS,MAJS1,MAJS2,MAJS3 = JS(security,check_date='2022-09-01',N=5,M1=5,M2=10,M3=20)
print('_JS的值为: {}'.format(_JS))
print('MAJS1的值为: {}'.format(MAJS1))
print('MAJS2的值为: {}'.format(MAJS2))
print('MAJS3的值为: {}'.format(MAJS3))



```





### 4.小结
GDX鬼道线

JS加速线

代码示例



## 4.趋向指标（下）
### 1.MA
:::info
即移动平均线指标，具有趋势特性。越长期的移动平均线，越能表现<font style="color:#DF2A3F;">稳定</font>的特性。移动平均线是一种<font style="color:#DF2A3F;">趋势追踪</font>工具，便于识别趋势已经终结或者反转，新的趋势是否正在形成。国内常用5日、10日、30日、60日、120日、250日线

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778660930302-8227542d-04b4-4fab-becc-ce35a9786a6e.png" width="688" title="" crop="0,0,1,1" id="ucec7fbf7" class="ne-image">



**葛兰碧法则**

> **买进信号：**
>
> 1.平均线从下降逐渐转为走平，而价格从下方突破平均线，为买进信号
>
> 
>
> 2.价格虽然跌破平均线，但是又立刻回升到平均线上，此时平均线仍然持续上升，仍为买进信号
>
> 
>
> 3.价格趋势走在平均线上，价格下跌并未跌破平均线且立刻反转上升，也是买进信号
>
> 
>
> 4.价格突然暴跌，跌破平均线，且远离平均线，则有可能反弹上升，也为买进时机
>
> 
>
> **卖出信号：**
>
> 1.平均线从上升逐渐转为盘局或下跌，而价格向下跌破平均线，为卖出信号
>
> 
>
> 2.价格虽然向上突破平均线，但是又立刻回跌至平均线下，此时平均线仍然持续的下降，仍为卖出信号
>
> 
>
> 3.价格趋势走在平均线下，价格上升并未突破平均线且立刻反转下跌，也是卖出信号
>
> 
>
> 4.价格突然暴涨，突破平均线，且远离平均线，则有可能反弹回跌，也为卖出时机
>



实现方式

:::info
from jqlib.technical_analysis import *

MA(security_list, check date, timeperiod=5, unit = '1d', include now = True, fq_ ref date = None)



<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">timeperiod</font>: 统计X日均线



示例

MA(security_list, check_date=' 2022-09-01' ,timeperiod = 5)

返回

MA

字典(dict):键(key)为股票代码，值(value)为数据

:::



### 2.VMA
:::info
即变异平均线，指每个交易日股票的开盘价、收盘价、最高价和最低价除以4的平均值。在股市中,当股价高于vma时，意味着股市较为强势，当股价低vma于时,就意味着股市处于弱势

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778661535363-9bf2a202-6f09-44c8-9d55-aefce9e50fbd.png" width="575" title="" crop="0,0,1,1" id="u64373f03" class="ne-image">

**二条以上平均线向上交叉时，****<font style="color:#DF2A3F;">进买</font>**

**二条以上平均线向下交叉时，****<font style="color:#DF2A3F;">卖出</font>**



实现方式

:::info
from jqlib.technical analysis import *

VMA(security_list, check_date, timeperiod = 12, unit = '1d',include_now = True, fq_ref_date = None)



security_list: 股票列表

check_date: 要查询数据的日期

timeperiod: 统计X日均线



示例

VMA(security_list, check_date=' 2022-09-01' ,timeperiod = 12)

返回

VMA

字典(dict): 键(key)为股票代码，值(value)为数据

常见多条VMA均线中进行比较，一般为6、12、24、72日VMA均线

:::



### 3.代码示例
```python
from jqlib.technical_analysis import *

#获得一只股票三天的5、10、20日均线
security = '000001.XSHE'
check_dates = ['2022-09-05','2022-09-06','2022-09-07']
for check_date in check_dates:
    MA5  = MA(security,check_date=check_date,timeperiod=5)
    MA10 = MA(security,check_date=check_date,timeperiod=10)
    MA20 = MA(security,check_date=check_date,timeperiod=20)
    
    print(check_date,'5 日均线:',MA5[security])
    print(check_date,'10日均线:',MA10[security])
    print(check_date,'20日均线:',MA20[security])
    
#获得一只股票三天的6/12/24/72日均线
print("--获得一只股票三天的6/12/24/72日均线---------------------")
security = '000001.XSHE'
check_dates = ['2022-09-05','2022-09-06','2022-09-07']
for check_date in check_dates:
    _VMA6 = VMA(security,check_date=check_date,timeperiod=6)
    _VMA12 = VMA(security,check_date=check_date,timeperiod=12)
    _VMA24 = VMA(security,check_date=check_date,timeperiod=24)
    _VMA72 = VMA(security,check_date=check_date,timeperiod=72)
    
    print(check_date,'6日变均线:',_VMA6[security])
    print(check_date,'12日变均线:',_VMA12[security])
    print(check_date,'24日变均线:',_VMA24[security])
    print(check_date,'72日变均线:',_VMA72[security])
```



### 小结
MA（移动平均线）

葛兰比法则

VMA（变异平均线）

代码示例



## 5.反趋向指标
### 1.RSI
:::info
即相对强弱指标，是期货市场和股票市场中最为<font style="color:#DF2A3F;">著名的摆动指标</font>。显示的是<font style="color:#DF2A3F;">股价向上波动的蝇度点总的波动幅度的百分</font>，如果其数值大，就表示市场处于强势状态，如果数值小，则表示市场处于弱势比，



**计算公式：**

N日RSI =A (A+B) x100

A=N日内收盘涨幅之和

B=N日内收盘跌幅之和(取正值)

由上再算式可知RSI指标的技术含义，即以向上的力量与向下的力量进行比校。

若向上的力量这大，则计算出来的指标上升；若向下的力量较大，则指标下降，由此测算出市场走势的强弱。



**应用：**

RSI>80为超买，RSI<20为超卖

RSI以50为中界线，大于50为多头行情，小于50为空头行情

RSI在80以上形成M头或头肩顶形态时，为向下反转信号

RSI在20以下形成W底或头肩底形态时，视为向上反转信号

RSI向上突破其高点连线时，买进；RSI向下跌破其低点连线时，卖出



**实现方式：**

from jqlib.technical analysis import *

RSI(security_list, check_date, N1=6, unit = '1d', include_now = True,fq_ref date = None)

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">N1</font>: 统计天数的值



示例

RSI(security_list, check_date=' 2022-09-01' ,N1=6)

返回

RSI

字典(dict):键(key)为股票代码，值(value)为数据

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778722342307-34918ab8-b836-485e-8ed7-24b86757c31e.png" width="767" title="" crop="0,0,1,1" id="ue49d79a4" class="ne-image">



### 2.WR
:::info
威廉指标(简称W%R)，它由拉瑞威廉首先发表。威廉指数主要用于研究股价的波动，通过分析<font style="color:#DF2A3F;">股价波动</font>变化中的<font style="color:#DF2A3F;">峰与谷</font>决定买卖时机，是用来分析市场<font style="color:#DF2A3F;">短期</font>行情走势的技术指标（用于短线指标）



**计算公式：**

W&R=(N日内最高价-当日收盘价) / (N日内最高价-N日内最低价)



**应用：**

当威廉指数线<font style="color:#DF2A3F;">高于80</font>，市场处于<font style="color:#DF2A3F;">超卖状态</font>，行情即将<font style="color:#DF2A3F;">见底</font>，<font style="color:#DF2A3F;">买进</font>

当威廉指数线<font style="color:#DF2A3F;">低于20</font>，市场处于<font style="color:#DF2A3F;">超买状态</font>，行情即将<font style="color:#DF2A3F;">见顶</font>，<font style="color:#DF2A3F;">卖出</font>

<font style="color:#DF2A3F;"></font>

**实现方式：**

from jqlib.technical analysis import *

WR(security_list, check date, N = 10, N1 = 6, unit = '1d', include _now= True, fq_ref date = None)

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">N,N1</font>: 统计天数的值



示例

WR(security_list, check_date=' 2022-09-01' ,N=14,N1=28)

返回

WR和MAWR字典(dict): 键(key)为股票代码，值(value)为数据

:::



<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778722578459-3354b749-6c2d-4577-9c0a-b0b9130929d9.png" width="776" title="" crop="0,0,1,1" id="ua0a9643e" class="ne-image">



### 3.KDJ
:::info
随机指标(KDJ)在设计中充分考虑<font style="color:#DF2A3F;">价格波动的随机振幅</font>与<font style="color:#DF2A3F;">中短期波动</font>的测算，使其短期测市功能比移动平均线更加准确有效，在市场短期<font style="color:#DF2A3F;">超买超卖</font>的预测方面又比相对强弱指标敏感。



**应用：**

K,D,J 均大于80，属于超买区，回档几率大

K,D,J 均小于30，属于超卖区，反弹几率大

K在20左右向上交叉D时，视为买进信号

K在80左右向下交叉D时，视为卖出信号

J>100时，股价易反转下跌；J<0时，股价易反转上涨

KDJ波动于50左右的任何信号，其作用不大



**代码实现：**

from jqlib.technical analysis import *

KDJ(security_list, check_date, N =9, M1=3, M2=3, unit = '1d',include_ now = True, fq_ref date = None)



security_list: 股票列表

check_date: 要查询数据的日期

N: 计算RSV的参数

M1: 计算K的M1日移动平均值

M2: 计算D的M1日移动平均值



示例

KDJ(security_list, check_date=' 2022-09-01' ,N =9, M1=3, M2=3)

返回

K、D、J

字典(dict):键(key)为股票代码，值(value)为数据

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778723215873-a91f5a38-33bb-46e2-a35f-14858f7f2ba5.png" width="389" title="" crop="0,0,1,1" id="u47f88701" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778723279729-5743d1a4-12e6-489b-b5d6-bd980d536569.png" width="707" title="" crop="0,0,1,1" id="u4bb5d859" class="ne-image">



### 4.代码实战
```python
from jqlib.technical_analysis import *

#获取多只股票的RSI值
print("--获取多只股票的RSI值----------------------------------------------")
security_list = ['000001.XSHE','000002.XSHE','601211.XSHG']
_RSI = RSI(security_list,check_date='2022-09-01',N1=6)

for stock in security_list:
    print(stock,'2022-09-01日RSI的值为:',_RSI[stock])
    

#获取单只股票的WR值
print("--获取单只股票的WR值----------------------------------------------")
security = '600031.XSHG'
check_dates = ['2022-10-31','2022-11-01','2022-11-02','2022-11-03']
for check_date in check_dates:
    _WR,_MAWR = WR(security,check_date=check_date,N=10,N1=3)
    print(check_date,'WR值为:',_WR[security])
    print(check_date,'MAWR值为:',_MAWR[security])
    
#获得单只股票的多日KDJ指标值
print("--获得单只股票的多日KDJ指标值----------------------------------------------")
security = '000001.XSHE'
check_dates = ['2022-09-05','2022-09-06','2022-09-07']
for check_date in check_dates:
    _K, _D, _J = KDJ(security,check_date=check_date,N=9,M1=3,M2=3)
    print(check_date,'_K值为:',_K[security])
    print(check_date,'_D值为:',_D[security])
    print(check_date,'_J值为:',_J[security])
```





### 小结
RSI

WR

KDJ

代码示例



## 6.压力支撑指标
### 1.BOLL（布林线指标）
:::info
即布林线指标，由约翰·布林先生创造，其利用统计原理，求出<font style="color:#DF2A3F;">股价的标准差及其信赖区间</font>，从而确定<font style="color:#DF2A3F;">股价的波动范围及未来走势</font>，利用<font style="color:#DF2A3F;">波带</font>显示股价的安全高低价位，因而也被称为<font style="color:#DF2A3F;">布林带</font>。其<font style="color:#DF2A3F;">上下限范围不固定</font>，随股价的滚动而变化



中间线=20日均线

Up线=20日均线+2SD(20日收市价)

Down线=20日均线-2SD(20日收市价)



**应用：**

股价上升穿越布林线上限时，回档机率大

股价下跌穿越布林线下限时，反弹机率大

布林线震动波带变窄时，表示变盘在即



代码实现：

from jqlib.technical analysis import*

Bollinger_Bands(security_list, check_date, timeperiod=20, nbdevup=2,nbdevdn=2, unit = '1d', include_now = True, fq_ref date = None)

<font style="color:#DF2A3F;">timeperiod</font>: X日均线

<font style="color:#DF2A3F;">nbdevup</font>: 计算上轨线时所用的指标，中轨线+X倍的标准差

<font style="color:#DF2A3F;">nbdevdn</font>: 计算下轨线时所用的指标，中轨线-X倍的标准差



示例

Bollinger_Bands(security_list, c

返回

上轨线UB、中轨线MB、下轨线LB

字典(dict):键(key)为股票代码，值(value)为数据

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778724774524-6e0424dc-5987-4f6d-b69b-e3532ea05ca9.png" width="854" title="" crop="0,0,1,1" id="u8f046cd6" class="ne-image">





### 2.MIKE（麦克指标）
:::info
麦克指标，其英文全称是“Mike Base”，是一种<font style="color:#DF2A3F;">股价波动幅度大小而变动</font>的压力支撑指标，设有<font style="color:#DF2A3F;">初级、中级、强力</font>三种不同级别的支撑和压力，用图标方式直接显示压力、支撑的位置



1、先求出真实值TPY

TPY=3(最高价+最低价+收盘价)

TPY一TPX之N天平均值

2、MIKE指标有三条初级、中级、强力压力、分别为WR、MR、SR.

WR=TPY+[TPY一(12天最低价)]

MR=TPY+(12天最高价一12天最低价)

SR=2x12天最高价一12天最低价

3、MIKE指标有三条初级、中级、强力压力、分别为WS、MS、Ss。

WS=TPY一(12天最高价一TPY)

MS=TPY一(12天最高价一12天最低价)

SS=2x12天最低价一12天最高价



**应用：**

MIKE指标共有六条曲线，上方三条压力线，下方三条支撑线

当股价脱离盘整，朝下跌的趋势前进时，股价下方三条“下限”为其支撑参考价

当股价脱离盘整，朝上涨的趋势前进时，股价上方三条“上限”为其压力参考价

当股价往压力线方向涨升时，其下方支撑线不具参考价值

当股价往支撑线方向下跌时，其上方压力线不具参考价值



实现方式

from jqlib.technical_analysis import *

MIKE(security_list, check_date, timeperiod = 10, unit = '1d',include_now = True, fq_ref date = None)

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">timeperiod</font>: 统计天数的值



示例

MIKE(security_list, check_date=' 2022-09-01' ,timeperiod=10)

返回

STOR MIDR WEKR WEKS MIDS STOS 的值

字典(dict):键(key)为股票代码，值(value)为数据



:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778725095947-64babbbe-9289-4fef-b2fb-5caf24f23c66.png" width="625" title="" crop="0,0,1,1" id="u3698bcc6" class="ne-image">





### 3.XS（薛斯通道）
:::info
薛斯通道指标是判断股价运行区间及相应的压力、支撑的趋势性指标。属于短线指标之一。由美国薛斯所创。在薛斯通道中股价实际上是被<font style="color:#DF2A3F;">短期小通道</font>包容着在<font style="color:#DF2A3F;">长期道</font>中上下运行，基本买卖策略是当<font style="color:#DF2A3F;">短期小通道接近长期大通道时，预示着趋势的近期反转。</font>

<font style="color:#DF2A3F;"></font>

**应用：**

在<font style="color:#DF2A3F;">上沿接近时趋势向下</font>反转可捕捉短期<font style="color:#DF2A3F;">卖点</font>

在<font style="color:#DF2A3F;">下沿接近时趋势向上</font>反转可捕捉短期<font style="color:#DF2A3F;">买点</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">实现代码：</font>**

<font style="color:#000000;">from jqlib.technical_analysis import *</font>

<font style="color:#000000;">XS(security_ list, check_date, timeperiod = 13, unit = '1d', include_ now= True, fq_ref date = None)</font>

<font style="color:#DF2A3F;">security_list</font><font style="color:#000000;">: 股票列表</font>

<font style="color:#DF2A3F;">check_date</font><font style="color:#000000;">: 要查询数据的日期</font>

<font style="color:#DF2A3F;">timeperiod</font><font style="color:#000000;">: 统计天数的值</font>

<font style="color:#000000;"></font>

<font style="color:#000000;">示例</font>

<font style="color:#000000;">XS(security_list, check_date=' 2022-09-01' ,timeperiod=13)</font>

<font style="color:#000000;">返回</font>

<font style="color:#000000;">SUP SDN LUP LDN 的值</font>

<font style="color:#000000;">字典(dict):键(key)为股票代码，值(value)为数据</font>

:::



<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778725545027-c09615dc-5f33-494c-8d60-88b92a31a9f5.png" width="539" title="" crop="0,0,1,1" id="uf7d02964" class="ne-image">



### 4.代码示例
```python
from jqlib.technical_analysis import *

#获得单只股票三天的BOLL指标值
print("--获得单只股票三天的BOLL指标值-----------------------------------")
security = '600031.XSHG'
check_dates = ['2022-10-31','2022-11-01','2022-11-02']
for check_date in check_dates:
    upper,middle,lower = Bollinger_Bands (security, check_date=check_date, timeperiod=20, 
        nbdevup=2, nbdevdn=2, unit='1d', include_now=True, fq_ref_date=None)
    print(check_date,f'{security}上轨道线值为:',upper[security])
    print(check_date,f'{security}中轨道线 值为:',middle[security])
    print(check_date,f'{security}下轨道线为:',lower[security])
    
#获得单只股票两天的MIKE指标值
print("--获得单只股票三两天的MIKE指标值-----------------------------------")
security = '600031.XSHG'
check_dates = ['2022-10-31','2022-11-01']
for check_date in check_dates:
    storl,midrl,wekrl,weksl,midsl,stosl = MIKE(security, check_date=check_date ,timeperiod=10)
    print(check_date,f'{security}的storl值为:',storl[security])
    print(check_date,f'{security}的midrl值为:',midrl[security])
    print(check_date,f'{security}的wekrl为:',wekrl[security])
    print(check_date,f'{security}的weksl为:',weksl[security])
    print(check_date,f'{security}的midsl为:',midsl[security])
    print(check_date,f'{security}的stosl为:',stosl[security])
    
#获得单只股票多日的XS指标值
print("--获得单只股票多日的XS指标值-----------------------------------")
security = '000001.XSHE'
check_dates = ['2022-10-31','2022-11-01']
for check_date in check_dates:
    SUP,SDN,LUP,LDN = XS(security,check_date=check_date,timeperiod=13)
    print(check_date,f'{security}的SUP 值为:',SUP[security])
    print(check_date,f'{security}的SDN值为:',SDN[security])
    print(check_date,f'{security}的LUP 为:',LUP[security])
    print(check_date,f'{security}的LDN为:',LDN[security])

```





### 小结
BOLL(布林线指标)

MIKE(麦克指标)

XS(薛斯通道)

代码示例



## 7.量价指标
## 1.OBV（能量潮指标）
:::info
能量潮指标是葛兰维于上世纪60年代提出的。OBV线系依据<font style="color:#DF2A3F;">成交量的变化</font>统计绘制而成。

OBV线为股市<font style="color:#DF2A3F;">短期波动</font>的重要判断方法，但运用OBV线应配合股价趋势予以研判分析



今日OBV = 昨日OBV+sgn*今天的成交量

其中，sgn是符号函数（正负1），其数值由下式决定:

sgn=+1，今日收盘价>昨日收盘价

sgn=-1，今日收盘价<昨日收盘价

这里的成交量指的是成交股票的手数，不是成交金额。

sng=+1时，其成交量计入多方的能量

sng=-1时，其成文量计入空方的能量

计算OBV时的初始值可自行确定，一般用第一日的成交量代替。



**应用：**

股价一顶比一顶高，而OBV一顶比一顶低，暗示头部即将形成

股价一底比一底低，而OBV一底比一底高，暗示底部即将形成

OBV突破其N字形波动的高点次数达<font style="color:#DF2A3F;">5次</font>时，为<font style="color:#DF2A3F;">短线卖点</font>

OBV跌破其N字形波动的低点次数达<font style="color:#DF2A3F;">5次</font>时，为<font style="color:#DF2A3F;">短线买点</font>

**<font style="color:#DF2A3F;">OBV不能单独使用</font>**<font style="color:#DF2A3F;">，</font><font style="color:#000000;">必须与股价曲线结合使用才能发挥作用</font>

<font style="color:#000000;"></font>

**<font style="color:#000000;">代码实现：</font>**

<font style="color:#000000;">from jqlib.technical analysis import *</font>

<font style="color:#000000;">OBV(security_list, check_date, timeperiod=30, unit = '1d',include_now = True, fq_ ref_date = None)</font>

<font style="color:#DF2A3F;">security_list</font><font style="color:#000000;">: 股票列表</font>

<font style="color:#DF2A3F;">check_date</font><font style="color:#000000;">: 要查询数据的日期</font>

<font style="color:#DF2A3F;">timeperiod</font><font style="color:#000000;">: 统计天数的值</font>

<font style="color:#000000;"></font>

<font style="color:#000000;">示例</font>

<font style="color:#000000;">OBV(security_list, check_date=' 2022-09-01' ,timeperiod=30)</font>

<font style="color:#000000;">返回</font>

<font style="color:#000000;">OBV</font>

<font style="color:#000000;">字典(dict):键(key)为股票代码，值(value)为数据</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778728038806-d67f3578-c245-4af1-aef0-201b80759184.png" width="811" title="" crop="0,0,1,1" id="uc7bea4de" class="ne-image">



## 2.VOL（成交量指标）
:::info
即成交量指标，成交量是指个股或大盘的成交总手，在形态上用一根立式的柱子来表示。左面的坐标值与柱子的横向对应处，就是当日当时的成交总数。如当天收盘价高于或等于当天的开盘价，成交柱呈红色;反之，成交柱呈绿色



VOL=EnVi/N

其中,i=1,2,3,.......n;

N=选定的时间参数,如10或30;

Vi:i日成交量。



**应用：**

1.当前股价处在盘整的行情的时候，成交量突然增加的话，股价短时间内突破的可能性较高

2.当成交量出现了连续三条或者更多的成交量的时候，说明当前市场买卖频繁，股价下跌的可能性比较的小

3.股价在上涨了一定的时间后，成交量依然是大幅上涨，但是最后收尾的时候，趋势阴线或者是比较小的阳线收尾的时候，说明当前上涨的支撑力量已经衰退，股价走势会在短时间内发生反转（<font style="color:#DF2A3F;">庄家撤退，散户买入</font>）



代码实现：

from jqlib.technical analysis import *

VOL(security list, check_date, M1=5, M2=10, unit = '1d', include_now= True, fq ref date = None)

<font style="color:#DF2A3F;">security_list</font>: 股票列表

<font style="color:#DF2A3F;">check_date</font>: 要查询数据的日期

<font style="color:#DF2A3F;">M1,M2</font>: 统计M1、M2日平均移动指数MAVOL的值



示例

VOL(security_list, check_date=' 2022-09-01' ,M1=5,M2=10)

返回

VOL、 MAVOL1 和MAVOL2

字典(dict):键(key)为股票代码，值(value)为数据



:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778728285934-32216c21-08eb-4fdc-b596-10a8ad825094.png" width="862" title="" crop="0,0,1,1" id="u9bf81356" class="ne-image">





### 3.代码示例
```python
from jqlib.technical_analysis import *

#获得多只股票多日的OBV（能量潮）指标值
print("--获得多只股票多日的OBV（能量潮）指标值--------------------------")
security_list = ['000001.XSHE','000002.XSHE','601211.XSHG']
check_dates = ['2022-10-31','2022-11-01']

for check_date in check_dates:
    for security in security_list:
        _OBV = OBV (security, check_date=check_date, timeperiod=30)
        print(check_date,f'{security}的OBV值为:', _OBV[security])



#获得多只股票多日的VOL（成交量指标）指标值
print("--获得多只股票多日的VOL（成交量指标）指标值--------------------------")
security_list = ['000001.XSHE','000002.XSHE']
check_dates = ['2022-10-31','2022-11-01']

for check_date in check_dates:
    for security in security_list:
        _VOL,MAVOL1,MAVOL2 = VOL (security, check_date=check_date, M1=5, M2=10)
        print(check_date,f'{security}的VOL值为:',_VOL[security])
        print(check_date,f'{security}的MAVOL1为:',MAVOL1[security])
        print(check_date,f'{security}的MAVOL2为:',MAVOL2[security])
```



### 小结
OBV（能量潮指标）

VOL（成交量指标）

代码示例



# 十一、量化策略回测
## 1.量化策略回测流程
### 1.量化策略回测整体流程
:::info
步骤1：选择股票池和实现回测函数

步骤2：设定回测时间段、初始金额、调仓频率

步骤3：历史数据载入（handle_data）

步骤4：处理订单

步骤5：取消未完成订单

步骤6：输出日志

步骤7：生成回测报告

:::



### 2.量化策略回测步骤分解
:::info
步骤1：选择股票池和实现回测函数，实现handle_data函数、编写量化策略

步骤2：选择回测开始时间和结束时间、选择初始金额、选择调仓频率

步骤3：取得股票数据，调用handle_data函数

步骤4：下单后，根据接下来时间的实际交易情况，处理订单

步骤5：下单后，可以调用get_open_orders取得所有未完成的订单，调用cancel_order取消订单

步骤6：回测结束，生成回测报告，画出收益曲线和基准收益曲线，列出每日持仓、交易数据指标等

:::



### 3.MACD策略示例
```python
import jqdata
import pandas as pd
from jqlib.technical_analysis import *


def initialize(context):
    #设定基准(沪深300)
    set_benchmark('000300.XSHG')
    #开启动态复权模式
    set_option('use_real_price', True)
    #标的股票
    g.security = '000001.XSHE'
    #设置macd默认值
    g.macd_yesterday = 0
    # ———— 新增：设置手续费和滑点（必须）————
    set_commission(PerTrade(buy_cost=0.0003, sell_cost=0.0013, min_cost=5)) 
    set_slippage(PriceRelatedSlippage(0.001)) 

# 进行操作的过程
def handle_data(context, data):
    security = g.security
    #计算当天的macd值
    DIF, DEA, _MACD = MACD(security_list=security,
                            check_date=context.current_dt,
                            SHORT=6,
                            LONG=12, 
                            MID=9)
    #获取当日现金
    cash = context.portfolio.cash
    #如果昨天的macd为负，今日macd为正，则表示出现金叉
    if g.macd_yesterday < 0 and _MACD[security] > 0 and cash > 0:
        order_value(security, cash)
    #如果昨天的macd为正，今日macd为负，则表示出现死叉
    elif g.macd_yesterday > 0 and _MACD[security] < 0 and \
            context.portfolio.positions[security].closeable_amount > 0:
        order_target(security, 0)

    g.macd_yesterday = _MACD[security]
```



## 2.MACD量化策略
### 1.MACD策略回顾
:::info
即平滑异同移动平均线，是由美国投资家杰拉尔德·阿佩尔在20世纪70年代末提出的，主要表示经过平滑处理后均线的差异程度。一般用来研判<font style="color:#DF2A3F;">股票价格变化的方向、强度和趋势</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">MACD如何判断金叉和死叉?</font>**

<font style="color:#000000;">快线DIF上穿慢线DEA，</font><font style="color:#DF2A3F;">红柱出现的第一天</font><font style="color:#000000;">，称为</font><font style="color:#DF2A3F;">金叉</font><font style="color:#000000;">，是</font><font style="color:#DF2A3F;">买进持有</font><font style="color:#000000;">的时机</font>

<font style="color:#000000;">快线DIF下穿慢线DEA，</font><font style="color:#DF2A3F;">绿柱出现的第一天</font><font style="color:#000000;">，称为</font><font style="color:#DF2A3F;">死叉</font><font style="color:#000000;">，是</font><font style="color:#DF2A3F;">卖出空仓</font><font style="color:#000000;">的时机</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778744252622-4d2f3246-65dc-4bd5-9e76-85dfda9f31ae.png" width="996" title="" crop="0,0,1,1" id="ue2432b47" class="ne-image">



### 2.MACD策略实现的思路
:::info
步骤1：导入函数库

步骤2：设定初始化函数

步骤3：计算每日现金与MACD

步骤4：根据MACD识别金叉与死叉

步骤5：根据买入卖出信号进行交易

:::



### 3.代码示例
```python
import jqdata
import pandas as pd
from jqlib.technical_analysis import *


def initialize(context):
    #设定基准(沪深300)
    set_benchmark('000300.XSHG')
    #开启动态复权模式
    set_option('use_real_price', True)
    #标的股票
    g.security = '000001.XSHE'
    #设置MACD初始化值
    g.macd_yesterday = 0
    # ———— 新增：设置手续费和滑点（必须）————
    set_commission(PerTrade(buy_cost=0.0003, sell_cost=0.0013, min_cost=5)) 
    set_slippage(PriceRelatedSlippage(0.001)) 

# 进行操作的过程
def handle_data(context, data):
    security = g.security
    #计算当天的macd值
    DIF, DEA, _MACD = MACD(security_list=security,
                            check_date=context.current_dt,
                            SHORT=6,
                            LONG=12, 
                            MID=9)
    #获取当日现金
    cash = context.portfolio.cash
    #如果昨天的macd为负，今日macd为正，则表示出现金叉
    if g.macd_yesterday < 0 and _MACD[security] > 0 and cash > 0:
        order_value(security, cash)
    #如果昨天的macd为正，今日macd为负，则表示出现死叉
    elif g.macd_yesterday > 0 and _MACD[security] < 0 and \
            context.portfolio.positions[security].closeable_amount > 0:
        order_target(security, 0)
    
    #更新当天MACD值
    g.macd_yesterday = _MACD[security]
```



## 3.量化回测风险指标（上）
### 1.风险指标介绍
:::info
即股票投资收益率的<font style="color:#DF2A3F;">不确定性</font>通常称之为<font style="color:#DF2A3F;">风险</font>，具体是指股imooc票市场的一些未知的、不可预测的因素对股票股价造成不确定的影响，可能是正面影响收益率,也可能是负面的背离。风险指标是对<font style="color:#DF2A3F;">风险的量化评价</font>。



**特点：**

风险指标有利于投资者对策略进行一个客观的评价。无论是回测还是模拟,所有风险指标都只会根据<font style="color:#DF2A3F;">每天收盘后的收益</font>计算每天更新一次，并<font style="color:#DF2A3F;">不考虑每天盘中的收益情况</font>。

:::



### 2.Alpha
:::info
Alpha是<font style="color:#DF2A3F;">投资者获得与市场波动无关的回报</font>。阿尔法系数，是基金/投资的绝对回报和按照beta系数计算的预期回报之间的差额。<font style="color:#DF2A3F;">阿尔法收益与风险相关性很低</font>。



**算法：**

<font style="color:#DF2A3F;">绝对收益</font>或<font style="color:#DF2A3F;">超额收益</font>是基金/投资的<font style="color:#DF2A3F;">实际收益减去无风险投资收益</font>。例如投资者获得了15%的回报,其基准获得了10%的回报,那么Alpha部分就是5%。

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746046265-455a6481-07ef-43e2-a23a-e77ec1141637.png" width="638" title="" crop="0,0,1,1" id="u834b0164" class="ne-image">

:::info
Alpha = 投资年化收益率 - [无风险回报率+Beta*(基准年化收益率-无风险回报率)]

:::



Alpha回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746120599-058a22da-9a93-4a31-802a-0a59844d23ea.png" width="1358" title="" crop="0,0,1,1" id="u82aa2533" class="ne-image">

### 3.Beta
:::info
Beta表示投资的系统性风险，反映了<font style="color:#DF2A3F;">策略对大盘变化的敏感性</font>。

例如一个策略的Beta为1.5,则大盘涨1%的时候,策略可能涨1.5%，

反之亦然;如果一个策略的Beta为-1.5,则大盘涨1%的时候，策略可能跌1.5%,反之亦然。

:::

**算法：**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746187074-1fe48025-db3f-4e25-9b35-cb8660c2a0c9.png" width="845" title="" crop="0,0,1,1" id="uba8529c0" class="ne-image">



**Beta回测：**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746218916-4d77c80a-a405-465a-9361-caa15fea35c0.png" width="1379" title="" crop="0,0,1,1" id="ub648f0dc" class="ne-image">

### 4.夏普比率
:::info
夏普(Sharpe)表示<font style="color:#DF2A3F;">每承受一单位总风险，会产生多少的超额报酬</font>，可以同时对策略的收益与风险进行综合考虑



**算法：**

夏普指数代表投资人每多承担一分风险，可以拿到较无风险报酬率(定存利率)高出几分的报酬;

若为<font style="color:#DF2A3F;">正值</font>，代表投<font style="color:#DF2A3F;">资承担报酬率波动风险有正的回馈</font>;

若为<font style="color:#DF2A3F;">负值</font>，代表承受风险但报酬率反而不如银行利率，<font style="color:#DF2A3F;">无参考意义</font>

:::



<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746376280-1141f61c-9247-4f16-953d-250ff2ef2b10.png" width="911" title="" crop="0,0,1,1" id="u37991684" class="ne-image">



夏普比率回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746414031-d787af22-33ae-40ce-b38e-ced42ebc4e2a.png" width="1348" title="" crop="0,0,1,1" id="u255c7de5" class="ne-image">



## 4.量化回测风险指标（中）
### 1.索提诺比率
:::info
Sortino(索提诺比率)表示<font style="color:#DF2A3F;">每承担一单位的下行风险将会获得多少超额回报</font>



算法：

与夏普比率有相似之处，但索提诺比率运用<font style="color:#DF2A3F;">下行波动率</font>而不是总标准差，以区别不利和有利的波动。

<font style="color:#DF2A3F;">这一比率越高，表明承担相同单位下行风险时能获得更高的超额回报率。</font>

索提诺比率可以看做是夏普比率在衡量股票风险的一种修正方式

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746704711-d5503684-d337-4a34-9bda-8c5b4266c3d9.png" width="844" title="" crop="0,0,1,1" id="u35ca04ee" class="ne-image">

索提诺比率回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746759529-ce05c9c0-4cd4-4a2c-85cf-2db640e6a716.png" width="1384" title="" crop="0,0,1,1" id="ue5b1b5a2" class="ne-image">



### 2.信息比率
:::info
Information Ratio(信息比率)用来衡量<font style="color:#DF2A3F;">单位超额风险带来的超额收益</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">算法：</font>**

<font style="color:#DF2A3F;">信息比率越大，说明该策略单位跟踪误差所获得的超额收益越高。</font>

<font style="color:#000000;">因此,信息比率较大的策略的表现要优于信息比率较低的基准。</font>

<font style="color:#000000;">合理的投资目标是在</font><font style="color:#DF2A3F;">承担适度风险下，尽可能追求高信息比率</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746864942-a9b56be6-888a-41cb-8ac7-48c69ec4edf1.png" width="1074" title="" crop="0,0,1,1" id="ua67531e6" class="ne-image">

信息比率回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778746898414-8a8db185-c68a-439f-8a05-3cf9574e95ce.png" width="1370" title="" crop="0,0,1,1" id="ufbd53c6d" class="ne-image">



### 3.策略波动率
:::info
策略波动率是衡量股票或者衍生品价格波动范围的指标，也通常被用来衡量风险。

一般的认为高波动率代表高风险，高风险对应高收益的可能。

:::

算法：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778747454381-159b24f7-ff10-4e8b-a0e8-8296a5c6ad13.png" width="663" title="" crop="0,0,1,1" id="uf71e6656" class="ne-image">



策略波动率回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778747486459-2628bd62-4bcd-4434-acd3-75916adb0458.png" width="1378" title="" crop="0,0,1,1" id="uccebe7e8" class="ne-image">



## 5.量化回测风险指标（下）
### 1.基准波动率
:::info
Benchmark Volatility(基准波动率)用来测量<font style="color:#DF2A3F;">基准的风险性，波动越大代表基准风险越高。</font>

:::

算法：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778748127615-bb2d4764-9443-4078-be03-6382b3cb3e78.png" width="821" title="" crop="0,0,1,1" id="u5209963b" class="ne-image">

基本波动率回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778748151025-833c8162-2230-47c1-9e01-a3bbb831db53.png" width="1364" title="" crop="0,0,1,1" id="ue53d7b87" class="ne-image">





### 2.最大回撤
:::info
最大回撤率是指在选定周期内任一历史时点往后推，股价走到最低点时的收益率回撤幅度的最大值。

<font style="color:#DF2A3F;">即在某一段时期内股价从最高点开始回落到最低点的幅度。</font>

<font style="color:#DF2A3F;">最大回撤用来描述买入股票后可能出现的最糟糕的情况</font>。最大回撤是一个重要的风险指标。

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778748219166-d2f7f478-c7b4-451b-abdb-c3a3ade38e17.png" width="670" title="" crop="0,0,1,1" id="u471dcf71" class="ne-image">

最大回撤回测：

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778748261658-e8b0684b-69df-4b2a-8a06-4107304da41c.png" width="1370" title="" crop="0,0,1,1" id="u722b2a8a" class="ne-image">



# 十二、因子分析
## 1.因子分析概述
### 1.因子分析概述
:::info
**定义：**

因子分析是股票投资的常用思路。指利用“因子”或特定特征”使各种股票收益最大化的投资方法。这些因素包括<font style="color:#DF2A3F;">波动性</font>、<font style="color:#DF2A3F;">动量</font>、<font style="color:#DF2A3F;">股票规模</font>等



**<font style="color:#000000;">原理：</font>**

因子分析将多个实测变量转换少数几个综合指标(或称潜变量)，它反映一种<font style="color:#DF2A3F;">降维</font>的思想。通过降维将相关性高的变量聚在一起，从而减少需要分析的变量的数量，而减少问题分析的复杂性。用来确定维度数量，对标体系的维度由主观来做判断

:::



### 2.因子类别和流程
:::info
**<font style="color:#000000;">量化选股因子：</font>**

多为<font style="color:#DF2A3F;">财务指标</font>，如<font style="color:#DF2A3F;">营业利润率、销售净利率、营业收入环比增长率</font>等

**量化择时因子：**

多为<font style="color:#DF2A3F;">技术指标</font>，如<font style="color:#DF2A3F;">均线、换手率、波动率</font>等 

**流程：**

<font style="color:#DF2A3F;">因子构造</font> -> <font style="color:#DF2A3F;">因子选股</font> -> <font style="color:#DF2A3F;">构建股票池</font> -> <font style="color:#DF2A3F;">策略回测</font>

:::



### 3.常用基础因子
:::info
**1.价量因子**

价量因子，是指利用<font style="color:#DF2A3F;">get_price()函数</font>可以获取到的价量信息，如open(开盘价)、close(收盘价)、high(最高价)、low(最低价)、volume(成交量)、money(成交金额)等

**2.财务数据因子**

财务数据因子，是指<font style="color:#DF2A3F;">当日可以看到的最新单季财务指标</font>，如peratio(动态市盈率)、turnover_ratio(换手率)、pb_ratio (市净率)、market_cap (股票的总市值)、circulating_market_cap(股票的流通市值)等

**3.行业因子**

行业因子包含<font style="color:#DF2A3F;">证监会行业分类</font>，<font style="color:#DF2A3F;">聚宽一、二级行业分类以及申万一二、三级行业分类</font>，如A01(农业)、A02(林业)、B06(煤炭开采和洗选业)、B07(石油和天然气开采业)、C36(汽车制造业)等。<font style="color:#000000;">返回值是一个</font><font style="color:#DF2A3F;">哑变量</font><font style="color:#000000;">，若某股票属于某行业，则返回1;否则返回0</font>

**<font style="color:#000000;">4.概念因子</font>**

<font style="color:#000000;">概念因子，即</font><font style="color:#DF2A3F;">概念板块代码</font><font style="color:#000000;">，如GN028(智能电网)、GN030物联网)、GN092(高端装备制造)、GN181(一带一路)等。返回值是一个</font><font style="color:#DF2A3F;">哑变量</font><font style="color:#000000;">，如果某股票属于某个概念，则返回1;否则返回0</font>

**<font style="color:#000000;">5.指数因子</font>**

<font style="color:#000000;">指数因子，即</font><font style="color:#DF2A3F;">指数代码</font><font style="color:#000000;">，如000001.XSHG(上证指数)、000002.XSHG(A股指数)、000003.XSHG(B股指数)、000006.XSHG(地产指数)等。返回值是一个</font><font style="color:#DF2A3F;">哑变量</font><font style="color:#000000;">，若某股票是某指数的成分股，则返回1;否则返回0</font>

**<font style="color:#000000;">6.资金流因子</font>**

<font style="color:#000000;">资金流因子，即getmoney_flow函数查询的数据。可以使用的字段包括:change_pct (涨跌幅)、net amount_ main (力净额)、net_pct_main (力净占比)、net_amount_xl (超大单净额)、net_pct_xl (超大单净占比)、net amount_1 (大单净额)、net_pct_1(大单净占比)、net_amount_m (中单净额)、net_ pct_m (中单净占比)net_amounts(小单净额)和net_pct_s(小单净占比)  （反应庄家占比）</font>

:::



### 小结
因子分析概述

因子类别及流程

常用基础因子



## 2.自定义因子实战
### 1.自定义因子
:::info
**自定义因子类：**

三个基本属性，分别为name、max_window 和dependencies;一个核心函数,calc()

**流程：**

构造因子属性 -> 实现因子计算 -> 因子分析



name:

因子名称。因子命名只能由字母、数字和下画线组成，并且第一个字符不能是数字，另外不能与Python中的HD关键字相同，也不能与基础因子冲突

max_window:

获取数据的最长时间窗口，返回日线数据

dependencies:

自定义因子依赖的基础因子名称，如high,low,close

:::



### 2.因子计算
:::info
实现方式：

实现Factor类内置calc(函数)

calc(self,data)



data: 字典对象

key属性是dependencies中的因子名称;

value属性是因子对应的数据表(pandas.DataFrame格式)



示例

def calc(self, data):

return data['close'][ -10:].mean()

返回

Pandas.Series:index属性是股票代码，value属性是因子值

:::



### 3.单因子分析
:::info
**实现方式：**

调用analyze_factor

analyze factor(

factor, 

start_date, 

end_date, 

industry, 

universe,

quantiles, 

periods, 

weight_ method, 

use _real_price, 

skip_paused,

max_loss, 

factor_dep_definitions

)



<font style="color:#DF2A3F;">factor</font>：获因子值，可输入三种类型的值

1. pandas.DataFrame:因子值,columns为股票代码 ('000001.XSHE') ,index为日期的Datetimelndex或str

2.pandas.Series:因子值，index为日期和股票代码的Multilndex

3.Fator的子类，自定义因子

<font style="color:#DF2A3F;">start_date</font>：开始日期

<font style="color:#DF2A3F;">end_date</font>：结束日期

<font style="color:#DF2A3F;">industry</font>：获行业分类，默认为jq_I1; sw11:申万一级行业;'sw I2:申万二级行业;sw 13:申万三级行业;jq11聚宽一级行业;jq12:聚宽二级行业;zjw:'证监会行业'

<font style="color:#DF2A3F;">universe</font>：对股票池的定义，可输入两种类型的值。为str时认为输入的是一个指数，股票池为这个指数的成分股，为list时认为输入的是一个股票池;当factor输入为因子值时(DataFrame、Series)，该参数无效

<font style="color:#DF2A3F;">quantiles</font>：分位数数量，默认为5

<font style="color:#DF2A3F;">periods</font>：调仓周期，int或int的列表，默认为[1,5,10]

<font style="color:#DF2A3F;">weight_method</font>：计算分位数收益时的加权方法;avg:按平均加权;mktcap:按市值加权

<font style="color:#DF2A3F;">use_real_price</font>：是否动态复权，默认为False(当factor为因子值时这个参数失效)

<font style="color:#DF2A3F;">skip_paused</font>：是否跳过停牌，默认为False(当factor为因子值时这个参数失效)

<font style="color:#DF2A3F;">maxloss</font>：因重复值或nan值太多而无效的因子值的最大占比，默认为0.25

<font style="color:#DF2A3F;">factor_dep_definitions</font>：主因子的依赖因子的列表，默认为空列表(注:当factor为因子值时这个参数失效

:::



### 4.代码示例
jupyter中运行以下代码

```python
from jqfactor import Factor,analyze_factor
warnings.filterwarnings('ignore')


class MA10(Factor):
    #因子名称为'ma10'
    name = 'ma10'
    #设定最长时间窗口
    max_window = 10
    #设置依赖的基础因子
    dependencies = ['close']
    #实现因子计算
    def calc(self,data):
        return data['close'][-10:].mean()


 #单因子分析

far = analyze_factor(factor=MA10,
                     start_date='2022-01-01',
                     end_date='2022-06-30',
                     weight_method='mktcap',
                     universe='000300.XSHG', 
                     industry='jq_11',
                     quantiles=8,
                     periods=(1,5,10))


#分析结束后通过不同属性获取数据
#月度信息系数
far.ic_monthly

''' 运行结果
        period_1	period_5	period_10
2022-01	-0.089596	-0.192517	-0.226488
2022-02	0.004491	0.011325	-0.054634
2022-03	-0.078828	-0.106743	-0.134678
2022-04	-0.029746	0.005308	0.058185
2022-05	-0.007236	0.080919	0.089145
2022-06	0.049581	0.125328	0.163221

'''
    
```





### 小结
自定义因子类

因子计算

单因子分析





## 3.因子分析结果
### 1.结果展示函数
:::info
**实现方式：**

create_full_tear_sheet(demeaned=False, group adjust=False,by_group=False, turnover_periods=None, avgretplot=(5, 15), std_bar=False)



<font style="color:#DF2A3F;">demeaned</font>：是否使用超额收益计算

True:使用超额收益计算(基准收益被认为是每日所有股票收益按照weight列中权重加权的均值)

False:不使用超额收益

<font style="color:#DF2A3F;">group_adjust</font>：是否使用行业中性化收益计算

False:不使用行业中性化后的收益

True:使用行业中性化后的收益计算(行业收益被认为是每日各个行业股票收益按照weight列中权重加权的均值)

<font style="color:#DF2A3F;">by_group</font>：是否按行业展示

True:按行业展示

False:不按行业展示

<font style="color:#DF2A3F;">turnover_periods</font>：调仓周期

<font style="color:#DF2A3F;">avgretplot</font>：tuple因子预测的天数(计算过去的天数，计算未来的天数)

<font style="color:#DF2A3F;">std_bar</font>：是否使用标准差

True:显示标准差

False:不显示标准差

:::



### 2.结果分析
:::info
**收益分析：**

因子收益分析。包含7种常见的收益分析。

**IC分析：**

指Information Coefficient,IC代表预测值和实现值之间的相关性，通常用以评价预测能力。取值在-1至1之间，值越大，表示预测能力越好

**换手率分析：**

因子的换手率是在不同的时间周期下，观察因子个分位中个股的进出情况



**收益分析详解：**

在收益分析中，分位数的平均收益，各分位数的累积收益，以及分位数的多空组合收益三方面观察因子的表现。<font style="color:#DF2A3F;">第一分位数的因子值最小，第五分位数的因子值最大</font>

<font style="color:#DF2A3F;"></font>

<font style="color:#DF2A3F;">分位数收益：</font><font style="color:#000000;">表示持仓1、5、10天后，各分位数可以获得的平均收益</font>

<font style="color:#DF2A3F;">分位数的累积收益：</font><font style="color:#000000;">表示各分位数持仓收益的累计值</font>

<font style="color:#DF2A3F;">多空组合收益：</font><font style="color:#000000;">做多五分位(因子值最大)，做空一分位(因子值最小)的投资组合的收益</font>

<font style="color:#000000;"></font>

**<font style="color:#000000;">IC分析：</font>**

<font style="color:#000000;">一般有两种方法，即normalIC和rankIC。聚宽量化交易平台计算的是rank IC</font>

<font style="color:#DF2A3F;">normalIC</font><font style="color:#000000;">：因子载荷与因子收益之间的相关系数</font>

<font style="color:#DF2A3F;">rankIC</font><font style="color:#000000;">：因子载荷的排序值与收益的排序值之间的相关系数</font>

<font style="color:#000000;">考虑到单日IC的波动较大，聚宽提供了KC的月度移动平均线作为参考</font>

<font style="color:#000000;"></font>

**<font style="color:#000000;">换手率分析：</font>**

<font style="color:#000000;">计算方法举例:</font>

<font style="color:#000000;">某因子第一分位持有的股票数量为30支，一天后有一只发生变动，其换手率为:1/30*100%=3.33%</font>

<font style="color:#000000;">对于5日、10日的换手率，在每日都会对比当日1、5分位数的成分股与5日、10日前该分位数的成分股的变化进行计算</font>

<font style="color:#000000;"></font>

**<font style="color:#000000;">价值：</font>**

<font style="color:#DF2A3F;">因子稳定性的体现</font><font style="color:#000000;">：换手率低的因子，因子值在时间序列层面的持续性更好</font>

<font style="color:#DF2A3F;">衡量交易成本</font><font style="color:#000000;">：在实际的交易过程中，假设我们要维护投资组合的因子暴露恒定，对于高换手率因子，则需要进行更多的交易。交易中的税费和滑点，也会吞噬掉我们的部分利润</font>

:::



### 3.代码示例
jupyter中运行以下代码

```python
from jqfactor import analyze_factor
from jqfactor import Factor
warnings.filterwarnings('ignore')

#自定义因子类
class MA5(Factor):
    name='ma5'
    max_window = 5
    dependencies = ['close']
    
    def calc(self,data):
        return data['close'][-5:].mean()
    
#进行单因子分析
far = analyze_factor(factor=MA5,
                     start_date= '2022-01-01',
                     end_date='2022-03-01',
                     weight_method= 'mktcap', 
                     universe='000300.XSHG', 
                     industry='jq_l1',
                     quantiles=8,
                     periods=(1,5,10))

#结果展示，绘制图表
far.create_full_tear_sheet(demeaned=False, 
                           group_adjust=False,
                           by_group=False, 
                           turnover_periods=None, 
                           avgretplot=(5,15),
                           std_bar=False)
```



### 小结
结果分析函数

结果分析

代码示例



## 4.Alpha因子
### 1.Alpha因子
:::info
**Alpha191:**

国泰君安数量化专题研究报告-《基于短周期价量特征的多因子选股imooc体系》给出了191个短周期交易型阿尔法因子。聚宽量化平台根据这份报告选取并实现了191个Alpha因子，并开源给大家使用。



**Alpha013:**

因子公式:((HIGH*LOW)^0.5)-VWAP)

:::



### 2.代码示例
jupyter中运行以下代码

```python
# 导入函数库
from jqfactor import Factor
import numpy as py
from jqfactor import analyze_factor

warnings.filterwarnings('ignore')

#自定义因子类
class ALPHA013(Factor):
    name ='alpha013'
    max_window = 1
    dependencies = ['high','low','volume','money']

    def calc(self,data):
        #最高价DF
        high = data['high']
        #最低价DF
        low = data['low']
        #计享vwap
        vwap = data['money']/data['volume']
        #计算因子值。
        return ((np.power(high*low,0.5)-vwap).mean())
    
#进行单因子分析
far = analyze_factor(factor=ALPHA013,
                     start_date= '2022-01-01',
                     end_date='2022-03-01',
                     weight_method= 'mktcap', 
                     universe='000300.XSHG', 
                     industry='jq_l1',
                     quantiles=8,
                     periods=(1,5,10))

#结果展示，绘制图表
far.create_full_tear_sheet(demeaned=False, 
                           group_adjust=False,
                           by_group=False, 
                           turnover_periods=None, 
                           avgretplot=(5,15),
                           std_bar=False)
```





# 十三、量化交易策略实战
## 1.双均线策略
### 1.双均线策略介绍
:::info
指两条不同周期的移动平均线，通过<font style="color:#DF2A3F;">短周期移动平均线和长周期移动平均线的相对大小</font>，研判买进与卖出时机的策略



5日均线向上突破10日均线，<font style="color:#DF2A3F;">金叉，买入</font>

5日均线向下突破10日均线，<font style="color:#DF2A3F;">死叉，卖出</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778826283656-99665cc1-86f4-4ba3-9be5-80614df73caa.png" width="1044" title="" crop="0,0,1,1" id="u8b4ab095" class="ne-image">





### 2.双均线策略实现思路
:::info
1.导入函数库

2.设定初始化函数

3.计算每日现金与移动MA

4.根据MA识别金叉与死叉

5.根据买入卖出信号进行交易

:::



### 3.代码示例
```python
"""
双均线策略
金叉时买入，死叉时卖出
"""
def initialize(context):
    g.security = "000333.XSHE"
    g.short_count = 5
    g.long_count = 10
    g.unit = "1d"
    run_daily(market_open, time="every_bar")
    
    
def market_open(context):
    #获取5日均线（当前和前一日）
    short_ma = get_ma(g.security, g.short_count, g.unit)
    #获取10日均线（当前和前一日）
    long_ma = get_ma(g.security, g.long_count, g.unit)
    
    #金叉时买入
    if get_golden_signal(short_ma, long_ma):
        print(f"金叉买入,MA{g.short_count}={short_ma},MA{g.long_count}={long_ma}")
        order_target(g.security, 100)
    
    #死叉时卖出
    elif get_death_signal(short_ma, long_ma):
        print(f"死叉卖出,MA{g.short_count}={short_ma},MA{g.long_count}={long_ma}")
        order_target(g.security, 0)
        
#计算MA
def get_ma(security:str, count:int, unit:str) -> list:
    #获取count+1的收盘价
    df = attribute_history(security,count+1,unit,["close"])
    
    #计算当前的ma
    now_ma = df[1:count+1]["close"].rolling(count).mean()[-1]
    #计算上次的ma
    pre_ma = df[:count]["close"].rolling(count).mean()[-1]
    
    return [pre_ma,now_ma]
        
"""
判断是否金叉
金叉:True
"""
def get_golden_signal(
    short_ma:list,
    long_ma:list
)->bool:
    return (short_ma[0] < long_ma[0] and short_ma[1] >= long_ma[1])
    
"""
判断是否死叉
死金叉:True
"""
def get_death_signal(
    short_ma:list,
    long_ma:list
)->bool:
    return (short_ma[0] > long_ma[0] and short_ma[1] < long_ma[1])
    
```



## 2.KDJ策略
### 1.KDJ量化策略介绍
:::info
随机指标(KDJ)在设计中充分考虑<font style="color:#DF2A3F;">价格波动的随机振幅</font>与<font style="color:#DF2A3F;">中短期波动</font>的测算，使其短期测市功能比移动平均线更加准确有效，在市场短期<font style="color:#DF2A3F;">超买超卖</font>的预测方面又比相对强弱指标敏感



K在20左右向上交叉D时，<font style="color:#DF2A3F;">买入股票</font>

K在80左右向下交叉D时，<font style="color:#DF2A3F;">全仓卖出</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1778832622834-100bcb4f-f82e-4170-acda-294ba416f03d.png" width="1224" title="" crop="0,0,1,1" id="ud03f447c" class="ne-image">



### 2.KDJ量化策略实现思路
:::info
1.导入函数库

2.设定初始化函数

3.实现开盘前函数

4.实现开盘时运行函数，识别交易信号进行交易

5.实现收盘后函数

:::



### 3.代码示例
```python
import jqdata
from jqlib.technical_analysis import *

"""
KDJ量化交易策略
超买超卖型技术指标KDJ
实现K在20左右向上交叉D时，全仓买入
K在80左右向下交叉D时，全仓卖出
"""

def initialize(context):
    #设定基准
    set_benchmark('000300.XSHG')
    #开启动态复权
    set_option('use_real_price',True)
    #设定股票交易费
    #买入时佣金万分之三
    #卖出时佣金万分之三加千分之一印花税
    #每笔交易最低扣5元
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ),type='stock')
    #开盘前运行
    run_daily(before_market_open,time='before_open',reference_security='000300.XSHG')
    #开盘时运行
    run_daily(market_open,time='open',reference_security='000300.XSHG')
    #收盘后运行
    run_daily(after_market_close,time='after_close',reference_security='000300.XSHG')
    
def before_market_open(context):
    #开盘前运行函数
    #输出运行时间
    log.info("当天交易开始")
    log.info("""before_market_open运行时间: {}""".format(str(context.current_dt.time())))
    #设定交易股票
    g.security = '000001.XSHE'
    
def market_open(context):
    #开盘时运行函数
    log.info("""market_open运行时间: {}""".format(str(context.current_dt.time())))
    security = g.security
    
    # 【核心优化】为了避免未来函数，我们获取前一个交易日的K、D值作为今天的交易依据
    # context.previous_date 会自动获取回测/实盘当前日期的上一个交易日
    yesterday = context.previous_date
    K1, D1 = KD(security, check_date=yesterday, N=9, M1=3, M2=3)
    
    #获取当前可用现金
    cash = context.portfolio.available_cash
    
    # 【核心修复】使用 get_price 获取该股票的最新实时价格（返回的是DataFrame格式）
    # fields='close' 表示获取最新成交价
    current_price_df = get_price(security, count=1, end_date=context.current_dt, frequency='1m', fields=['close'])
    
    # 防御性编程：防止因停牌或无行情导致获取不到价格而报错
    if current_price_df is None or current_price_df.empty:
        log.info("无法获取{}的实时行情，今日跳过交易".format(security))
        return
        
    current_price = current_price_df['close'][0]
    
    #识别买入信号：若昨日K值在20左右且向上交叉D，则今日开盘全仓买入
    if K1[security] >= 20 and K1[security] > D1[security]:
        # 计算买入一手（100股）所需的最低资金
        min_buy_cash = current_price * 100
        
        # 资金门槛判断
        if cash >= min_buy_cash:
            log.info("买入股票{}，当前价格: {:.2f}，可用资金: {:.2f}".format(security, current_price, cash))
            order_value(security, cash)
        else:
            log.info("资金不足以买入一手{}，当前价格: {:.2f}，可用资金: {:.2f}".format(security, current_price, cash))
        
    #识别卖出信号：若昨日K值在80左右且向下交叉D，并且目前有可卖头寸，则全仓卖出
    # 增加判断：security in context.portfolio.positions 确保当前持有该股票
    elif (K1[security] < 80 and K1[security] < D1[security] and 
          security in context.portfolio.positions and 
          context.portfolio.positions[security].closeable_amount > 0):
        log.info("卖出股票{}，当前价格: {:.2f}".format(security, current_price))
        order_target(security, 0)
        
def after_market_close(context):
    #收盘后运行函数
    #输出运行时间
    log. info("""after_market_close: {}""".format(str(context.current_dt.time())))
    #得到当天所有成交记录
    trades = get_trades()
    for _trade in trades.values():
        log.info("""成交记录:{}""".format(str(_trade)))
        
    log.info("当天交易结束")
```





## 3.MA-RSI量化交易策略
### 1.MA-RSI量化交易策略介绍
:::info
**MA-RSI策略：**

利用<font style="color:#DF2A3F;">MA、RSI</font>这两个常见指标，选出上升趋势的超卖个股，同时缩小了选股范围，用一些简单的卖出和止损策略，就能达到稳定的收益



**选股范围：**

选取市值大于<font style="color:#DF2A3F;">500亿</font>的股(胜率相对较高)，排除st、科创板、创业板、退市、次新股股票，按净利润环比增长率降序排列



**买卖信号：**

K线在MA-200均线上方，RSI-10小于25，<font style="color:#DF2A3F;">买入股票</font>

RSI-10大于40;持有股票第N天;个股下跌超过5%;<font style="color:#DF2A3F;">卖出</font>

:::



### 2.MA-RSI量化策略实现思路
:::info
1、导入函数库，设定初始化函数

2、过滤无效股票，根据MA-RSI指标信号选股

3、根据交易信号交易，支持风控

:::



### 3.代码实战
```python
# MA-RSI里化交易策略
from jqdata import *
from jqlib.technical_analysis import *
import numpy as np
import pandas as pd

#初始化函数
def initialize(context):
    #设定基准
    set_benchmark('000300.XSHG')
    #设置开启避免未来数据模式
    set_option("avoid_future_data",True)
    #开启动态复权，使用真实价格
    set_option('use_real_price',True)
    #设定成交量比例
    set_option('order_volume_ratio',1)
    
    #设定股票交易费
    #买入时佣金万分之三
    #卖出时佣金万分之三加千分之一印花税
    #每笔交易最低扣5元
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ),type='stock')
    
    #持仓数量
    g.stock_num = 10
    #持仓天数
    g.hold_cnt = 0
    #运行函数
    run_daily(trade,time='14:50',reference_security='000300.XSHG')
    
    
#选股
def check_stocks(context):
    #获取当天时间
    now = context.current_dt
    #创建买入股票池
    g.buylist=[]
    #获取目标股票
    security_list = get_all_stock(context,now,200)
    #筛选股票
    q = query(valuation.code).filter(
        valuation.code.in_(security_list),
        valuation.market_cap > 500 # 市大于500亿
    ).order_by(
        indicator.inc_net_profit_annual.desc()  #按净利润同比增长率降序排列
    )
    
    security_list = list(get_fundamentals(q).code)
    #获取现价
    h = get_bars(security_list,count=1,unit='1d',end_dt=now,fields=['close'], include_now=True)
    #获取MA200
    MA200 = MA(security_list,check_date=now,timeperiod=200,unit='1d',include_now=True)
    #获骏RSI10
    RSI10 = RSI(security_list,check_date=now,N1=10)
    
    #条件选股
    for security in security_list:
        #收盘份高于MA200
        MA_True = h[security]['close'] > MA200[security]
        #RSI小于25
        RSI_True = RSI10[security] < 25
        #获取股票池
        if MA_True and RSI_True:
            g.buylist.append(security)
            if len(g.buylist) == g.stock_num:
                break
    
    log.info('今日买入股票:'+str(g.buylist))
    return g.buylist
    
#获取目标股票，过滤st、科创板、创业板、退市、次新股
def get_all_stock(context,now,ndays):
    df = get_all_securities(types=['stock'],date=now)
    df = df[(~df['display_name'].str.contains("ST")) &
            (~df['display_name'].str.contains("退")) & 
            (~df['display_name'].str.contains("\*")) &
            ((df.index.str[0:3]!='300') &
            (df.index.str[0:3]!='688'))
            ]
    #判断上市天数是否满足要求
    return [str(stock) for stock in df.index if (now.date()-df.loc[stock,'start_date']).days > ndays]
    
# 交易
def trade(context):
    log.info('天数:'+str(g.hold_cnt))
    #获取当天时间
    now = context.current_dt
    #获取持仓股票
    holding_list = list(context.portfolio.positions.keys())
    #获取持仓股票现价
    h = get_bars(holding_list,count=1,unit='1d',end_dt=now,fields=['close'],include_now=True)
    
    #根据策略交易
    #没有持仓,买入目标股票
    if len(holding_list) == 0:
        buy_list = check_stocks(context)
        for security in buy_list:
            cash = context.portfolio.cash/len(buy_list)
            order_value(security,cash)
            g.hold_cnt = 1
            log.info('买入股票:'+str(security))
        
    #根据卖出策略卖出(持仓超过11天;RSI>40;下跌超过-5%)
    elif g.hold_cnt > 0 and g.hold_cnt < 11:
        g.hold_cnt += 1
        for security in holding_list:
            RSI10 = RSI(security,check_date=now,N1=10)
            current_price = h[security]['close']
            cost = context.portfolio.positions[security].avg_cost
            if RSI10[security] > 40 or current_price < 0.95 * cost:
                order_target_value(security,0)
                log.info('卖出股票:'+str(security))
            else:
                break
    #持仓时间到达11天，卖出持仓股票
    elif g.hold_cnt == 11:
        buy_list = check_stocks(context)
        for security in holding_list:
            if security not in buy_list: # 卖出股票，判断是否不在买入目标股票
                order_target_value(security,0)
                log.info('卖出股票:'+str(security))
                g.hold_cnt = 0
        for security in buy_list:
            if security not in holding_list: # 买出股票，判断是否不在持仓股票池
                cash = context.portfolio.cash / len(buy_list)
                order_value(security,cash)
                g.hold_cnt = 1
                log.info('买入股票:'+str(security))
    else:
        log.info("出错啦！！！")
    
```

> AI诊断：
>

| <font style="color:rgb(15, 17, 21);">问题类型</font> | <font style="color:rgb(15, 17, 21);">原代码问题</font> | <font style="color:rgb(15, 17, 21);">修改方案</font> | <font style="color:rgb(15, 17, 21);">重要性</font> |
| --- | --- | --- | --- |
| <font style="color:rgb(15, 17, 21);">未来函数</font> | `<font style="color:rgb(15, 17, 21);">include_now=True</font>` | <font style="color:rgb(15, 17, 21);">全部改为</font>`<font style="color:rgb(15, 17, 21);">False</font>` | <font style="color:rgb(15, 17, 21);">🔴</font><font style="color:rgb(15, 17, 21);"> 致命</font> |
| <font style="color:rgb(15, 17, 21);">逻辑错误</font> | `<font style="color:rgb(15, 17, 21);">else: break</font>` | <font style="color:rgb(15, 17, 21);">删除break，遍历所有股票</font> | <font style="color:rgb(15, 17, 21);">🔴</font><font style="color:rgb(15, 17, 21);"> 严重</font> |
| <font style="color:rgb(15, 17, 21);">空列表崩溃</font> | <font style="color:rgb(15, 17, 21);">无检查直接使用</font> | <font style="color:rgb(15, 17, 21);">增加</font>`<font style="color:rgb(15, 17, 21);">if len() > 0</font>`<br/><font style="color:rgb(15, 17, 21);">判断</font> | <font style="color:rgb(15, 17, 21);">🟡</font><font style="color:rgb(15, 17, 21);"> 中等</font> |
| <font style="color:rgb(15, 17, 21);">数据缺失崩溃</font> | <font style="color:rgb(15, 17, 21);">直接索引字典</font> | <font style="color:rgb(15, 17, 21);">使用</font>`<font style="color:rgb(15, 17, 21);">.get()</font>`<br/><font style="color:rgb(15, 17, 21);">和</font>`<font style="color:rgb(15, 17, 21);">pd.isna()</font>` | <font style="color:rgb(15, 17, 21);">🟡</font><font style="color:rgb(15, 17, 21);"> 中等</font> |
| <font style="color:rgb(15, 17, 21);">正则表达式</font> | `<font style="color:rgb(15, 17, 21);">"\*"</font>`<br/><font style="color:rgb(15, 17, 21);">未转义</font> | <font style="color:rgb(15, 17, 21);">使用</font>`<font style="color:rgb(15, 17, 21);">r"\*"</font>` | <font style="color:rgb(15, 17, 21);">🟢</font><font style="color:rgb(15, 17, 21);"> 轻微</font> |
| <font style="color:rgb(15, 17, 21);">板块过滤</font> | <font style="color:rgb(15, 17, 21);">切片比较</font> | <font style="color:rgb(15, 17, 21);">使用</font>`<font style="color:rgb(15, 17, 21);">startswith()</font>` | <font style="color:rgb(15, 17, 21);">🟢</font><font style="color:rgb(15, 17, 21);"> 优化</font> |


修改后的代码：

```python
# MA-RSI量化交易策略（完整修正版）
from jqdata import *
from jqlib.technical_analysis import *
import numpy as np
import pandas as pd

#初始化函数
def initialize(context):
    #设定基准
    set_benchmark('000300.XSHG')
    #设置开启避免未来数据模式
    set_option("avoid_future_data", True)
    #开启动态复权，使用真实价格
    set_option('use_real_price', True)
    #设定成交量比例
    set_option('order_volume_ratio', 1)
    
    #设定股票交易费
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')
    
    # 持仓数量
    g.stock_num = 10
    # 记录每只股票的买入日期 {股票代码: 买入日期}
    g.buy_date = {}
    # 买入阈值
    g.buy_threshold = 25
    # 卖出阈值
    g.sell_threshold = 40
    # 最大持仓天数
    g.max_hold_days = 11
    # 止损比例
    g.stop_loss = 0.95
    
    #运行函数
    run_daily(trade, time='14:50', reference_security='000300.XSHG')
    
# 选股函数
def check_stocks(context):
    #获取当天时间
    now = context.current_dt
    #创建买入股票池
    buy_list = []
    
    #获取目标股票池（过滤ST、科创板、创业板、退市、次新股）
    security_list = get_all_stock(context, now, 200)
    
    if len(security_list) == 0:
        log.info('没有符合条件的股票')
        return []
    
    #筛选市值大于500亿的股票
    q = query(valuation.code).filter(
        valuation.code.in_(security_list),
        valuation.market_cap > 500
    ).order_by(
        indicator.inc_net_profit_annual.desc()
    )
    
    security_list = list(get_fundamentals(q).code)
    
    if len(security_list) == 0:
        log.info('市值过滤后没有股票')
        return []
    
    #分批获取数据
    batch_size = 50
    all_ma200 = {}
    all_rsi10 = {}
    all_prices = {}
    
    for i in range(0, len(security_list), batch_size):
        batch = security_list[i:i+batch_size]
        try:
            # 【修改1】include_now=False，避免未来函数
            prices = get_bars(batch, count=1, unit='1d', end_dt=now, 
                            fields=['close'], include_now=False, df=False)
            for sec in batch:
                if sec in prices and not pd.isna(prices[sec]['close']):
                    all_prices[sec] = prices[sec]['close']
            
            # 【修改1】include_now=False，使用已完成的K线
            ma200 = MA(batch, check_date=now, timeperiod=200, unit='1d', include_now=False)
            for sec, value in ma200.items():
                if not pd.isna(value):
                    all_ma200[sec] = value
            
            # 【修改1】include_now=False，使用已完成的K线
            rsi10 = RSI(batch, check_date=now, N1=10, unit='1d', include_now=False)
            for sec, value in rsi10.items():
                if not pd.isna(value):
                    all_rsi10[sec] = value
            
        except Exception as e:
            log.error(f'获取数据失败: {e}')
            continue
    
    #条件选股
    for security in security_list:
        # 【修改3】使用.get()防御性获取，避免KeyError
        price = all_prices.get(security)
        ma200_val = all_ma200.get(security)
        rsi_val = all_rsi10.get(security)
        
        # 数据完整性检查
        if price is None or ma200_val is None or rsi_val is None:
            continue
            
        try:
            #收盘价高于MA200
            ma_true = price > ma200_val
            #RSI小于买入阈值
            rsi_true = rsi_val < g.buy_threshold
            
            if ma_true and rsi_true:
                buy_list.append(security)
                if len(buy_list) == g.stock_num:
                    break
        except Exception as e:
            continue
    
    log.info('今日买入股票:' + str(buy_list))
    return buy_list
    
# 获取目标股票，过滤st、科创板、创业板、退市、次新股
def get_all_stock(context, now, ndays):
    df = get_all_securities(types=['stock'], date=now)
    # 【修改4】修正正则表达式，使用r"\*"匹配星号
    df = df[(~df['display_name'].str.contains("ST", na=False)) &
            (~df['display_name'].str.contains("退", na=False)) & 
            (~df['display_name'].str.contains(r"\*", na=False)) &
            (~df.index.str.startswith(('300', '688')))]  # 优化创业板/科创板过滤
    
    result = []
    for stock in df.index:
        try:
            if (now.date() - df.loc[stock, 'start_date']).days > ndays:
                result.append(str(stock))
        except:
            continue
    
    return result

# 计算某只股票的持仓天数
def get_hold_days(context, security):
    """返回股票的持仓天数，如果没有记录则返回0"""
    if security in g.buy_date:
        return (context.current_dt.date() - g.buy_date[security]).days
    return 0

# 交易函数
def trade(context):
    #获取当天时间
    now = context.current_dt
    #获取持仓股票
    holding_list = list(context.portfolio.positions.keys())
    
    log.info('=' * 50)
    log.info('当前持仓股票: ' + str(holding_list))
    for stock in holding_list:
        hold_days = get_hold_days(context, stock)
        log.info(f'{stock} 持仓天数: {hold_days}')
    
    # ========== 第一步：检查每只持仓股票是否需要卖出 ==========
    stocks_to_sell = []
    
    if len(holding_list) > 0:
        try:
            # 【修改1】include_now=False，避免未来函数
            current_prices = get_bars(holding_list, count=1, unit='1d', end_dt=now,
                                    fields=['close'], include_now=False, df=False)
            # 【修改1】include_now=False，避免未来函数
            rsi_values = RSI(holding_list, check_date=now, N1=10, unit='1d', include_now=False)
        except Exception as e:
            log.error(f'获取持仓数据失败: {e}')
            return
        
        # 【修改2】删除else:break，遍历所有持仓股票
        for security in holding_list:
            # 【修改3】防御性数据获取
            price_data = current_prices.get(security)
            rsi_val = rsi_values.get(security)
            
            if price_data is None or rsi_val is None or pd.isna(rsi_val):
                log.warning(f'{security} 数据缺失，跳过检查')
                continue
            
            current_price = price_data['close']
            if pd.isna(current_price):
                log.warning(f'{security} 价格缺失，跳过检查')
                continue
                
            cost = context.portfolio.positions[security].avg_cost
            hold_days = get_hold_days(context, security)
            
            # 卖出条件1：持仓达到11天
            if hold_days >= g.max_hold_days:
                stocks_to_sell.append(security)
                log.info(f'{security} 持仓已达{hold_days}天，达到最大持仓天数{g.max_hold_days}天，卖出')
            
            # 卖出条件2：RSI大于40
            elif rsi_val > g.sell_threshold:
                stocks_to_sell.append(security)
                log.info(f'{security} RSI={rsi_val:.2f} > {g.sell_threshold}，卖出')
            
            # 卖出条件3：下跌超过-5%（止损）
            elif current_price < g.stop_loss * cost:
                stocks_to_sell.append(security)
                log.info(f'{security} 价格{current_price:.2f} < 成本{cost:.2f}*{g.stop_loss}，止损卖出')
    
    # 执行卖出
    for security in stocks_to_sell:
        order_target_value(security, 0)
        # 删除买入日期记录
        if security in g.buy_date:
            del g.buy_date[security]
        log.info('卖出股票:' + str(security))
    
    # ========== 第二步：更新持仓列表 ==========
    holding_list = list(context.portfolio.positions.keys())
    
    # ========== 第三步：买入新股票（如果有空余仓位） ==========
    if len(holding_list) < g.stock_num:
        # 获取符合条件的买入股票池
        potential_buy_list = check_stocks(context)
        
        # 【修改3】增加长度检查，防止空列表导致的问题
        if len(potential_buy_list) > 0:
            # 过滤掉已经在持仓中的股票
            new_buy_list = [s for s in potential_buy_list if s not in holding_list]
            
            # 计算还可以买入多少只股票
            available_slots = g.stock_num - len(holding_list)
            new_buy_list = new_buy_list[:available_slots]
            
            if len(new_buy_list) > 0:
                # 计算每只股票的买入金额
                total_stocks = len(holding_list) + len(new_buy_list)
                cash_per_stock = context.portfolio.cash / total_stocks if total_stocks > 0 else 0
                
                # 重新平衡现有持仓（可选，保持仓位均衡）
                if len(holding_list) > 0 and cash_per_stock > 0:
                    for security in holding_list:
                        order_target_value(security, cash_per_stock)
                
                # 买入新股票
                for security in new_buy_list:
                    if cash_per_stock > 0:
                        order_value(security, cash_per_stock)
                        # 记录买入日期
                        g.buy_date[security] = context.current_dt.date()
                        log.info(f'买入股票:{security}，买入日期:{g.buy_date[security]}')
        else:
            log.info('没有符合条件的买入股票')
    
    # ========== 第四步：输出最终持仓信息 ==========
    final_holding = list(context.portfolio.positions.keys())
    log.info('最终持仓: ' + str(final_holding))
    for stock in final_holding:
        log.info(f'  {stock} 持仓天数: {get_hold_days(context, stock)}')
    log.info('=' * 50)
```



## 4.能量型指标量化交易策略
### 1.能量型指标量化策略介绍
:::info
**能量型指标：**

能量型指标，即情绪指标BR、AR、中间意愿CR、成交量变异率VR



**买卖信号：**

当AR<100、BR<100、BR<AR、CR<100、VR<100时，<font style="color:#DF2A3F;">买入股票</font>

当AR>150、BR>150、CR>150、VR>150<font style="color:#DF2A3F;">,卖出股票</font>

:::



### 2.能量型指标量化策略实现思路
:::info
1、导入函数库，设定初始化函数

2、计算能量型指标及现金

3、计算交易信号，并进行交易

:::



### 3.代码示例
```python
#能量型指标量化交易策略
from jqdata import *
from jqlib.technical_analysis import *


#初始化函数
def initialize(context):
    #选定交易股票
    g.security = '000001.XSHE'
    #设定基准
    set_benchmark('000300.XSHG')
    #开启动态复权模式(真实价格)
    set_option('use_real_price',True)
    #设定股票交易费
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')
    
#盘中运行函数
def handle_data(context, data):
    #计算能量指标
    security = g.security
    
    #计算情绪指标BRAR
    BR1, AR1 = BRAR(security, check_date=context.current_dt, N=26)
    
    #计算中间意愿指标CR
    CR1, MA1, MA2, MA3, MA4 = CR(security, check_date=context.current_dt, N=26, M1=10, M2=20, M3=40, M4=80)
    
    #计算成交量变异率指标VR
    VR1, MAVR1 = VR(security, check_date=context.current_dt, N=26, M=6)
    
    #取得当前现金
    cash = context.portfolio.cash

    #识别买入信号
    if (AR1[security] < 100 and 
        BR1[security] < 100 and 
        BR1[security] < AR1[security] and 
        CR1[security] < 100 and 
        VR1[security] < 100 and 
        cash > 0):
        # 买入股票
        order_value(security, cash)
        #记录日志
        log.info("买入股票%s" % (security))
        
    #识别卖出信号
    elif (AR1[security] > 150 and 
          BR1[security] > 150 and
          CR1[security] > 150 and 
          VR1[security] > 150 and 
          context.portfolio.positions[security].closeable_amount > 0):
        # 全部卖出股票
        order_target(security, 0)
        #记录日志
        log.info("卖出股票%s" % (security))
```



## 5.BOLL量化交易策略
### 1.BOLL量化策略介绍
:::info
**BOLL指标：**

在股市分析软件中，<font style="color:#DF2A3F;">BOLL指标一共由四条线组成</font>，即<font style="color:#DF2A3F;">上轨线UP</font>、<font style="color:#DF2A3F;">中轨线MB</font>、<font style="color:#DF2A3F;">下轨线DN</font>和<font style="color:#DF2A3F;">价格线</font>。其中上轨线UP是UP数值的连线;中轨线MB是MB数值的连线;下轨线DN是DN数值的连线;

在实战中，投资者主要了解<font style="color:#DF2A3F;">BOLL指标原理及如何运用</font>，以便更加深入地掌握BOLL指标的实质，为运用指标打下基础。



**策略原理：**

当股价<font style="color:#DF2A3F;">穿越最外面的压力线(支撑线)时</font>,表示<font style="color:#DF2A3F;">卖点(买点)出现</font>

当<font style="color:#DF2A3F;">股价延着压力线(支撑线)上升(下降)运行</font>,虽然股价并未穿越，但<font style="color:#DF2A3F;">若回头突破第二条线即是卖点或买点</font>

****

**买卖信号：**

<font style="color:#DF2A3F;">当收盘价格穿越BOLL的压力线，买入股票</font>

<font style="color:#DF2A3F;">当收盘价格穿越BOLL的支撑线，卖出股票</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1779086631158-77f1e94a-72c0-4628-880e-dcec889a7ded.png" width="1258" title="" crop="0,0,1,1" id="u06c0fcb0" class="ne-image">



### 2.BOLL量化策略实现思路
:::info
1、导入函数库，设定初始化函数

2、计算BOLL指标及现金

3、计算交易信号，并进行交易

:::



### 3.代码示例
```python
#能量型指标量化交易策略
from jqdata import *
from jqlib.technical_analysis import *


#初始化函数
def initialize(context):
    #设定基准
    set_benchmark('000300.XSHG')
    #开启动态复权模式(真实价格)
    set_option('use_real_price',True)
    #设定股票交易费
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')
    
    # 设置交易股票
    g.security = '002389.XSHE'
    # 设置N取值
    g.k = 2
    
#盘中BOLL量化策略
def handle_data(context, data):
    #获取该股票20日收盘价
    sr = attribute_history(g.security, 20)['close']
    #获取该股票20日均价
    ma = sr.mean()
    #up线(压力线):20日均线+N*SD(20日收盘价标准差)
    up = ma + g.k * sr.std()
    #down线(支撑线):20日均线-N*SD(20日收盘价标准差)
    down = ma - g.k * sr.std()
    
    #获取股票的开盘价格
    p = get_current_data()[g.security].day_open
    #获取当前现金
    cash = context.portfolio.available_cash
    #持仓标的信息
    #买入信号:跌破下线且没有持仓
    if p < down and g.security not in context.portfolio.positions:
        order_value(g.security, cash)
    #卖出信号:涨破上线且有持仓
    elif p > up and g.security in context.portfolio.positions:
        order_target(g.security, 0)

```



## 6.新能源股票轮动股票化交易策略
### 1.新能源股票轮动量化交易策略介绍
:::info
**策略基础：**

股市中，热点板块指的是当前市场上交投比较活跃，成交量比较大，板块内个股活跃度高于市场平均水平的行业或地域板块降。新能源属于热点板块，该板块中的股票更替快速，普遍收益较高。

**策略原理：**

<font style="color:#DF2A3F;">始终持有新能源指数成分股中市净率最低的股票</font>，每周检查一次

<font style="color:#DF2A3F;">若发现有新的新能源股票的市净率低于原有的股票</font>，则予以换仓

:::



### 2.新能源股票轮动量化交易策略实现思路
:::info
1、导入函数库，设定初始化函数

2、实现策略选股

3、实现策略交易

:::



### 3.代码示例
```python
from jqdata import *
from jqlib.technical_analysis import *


#初始化函数
def initialize(context):
    #设定基准
    set_benchmark('000300.XSHG')
    #开启动态复权模式(真实价格)
    set_option('use_real_price',True)
    #设定成交量比例
    set_option('order_volume_ratio',1)
    #设定股票交易费
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')
    # 运行函数
    # 选股运行策略
    run_weekly(check_stocks, weekday=1, time='before_open')
    # 交易
    run_weekly(trade, weekday=1, time='open')

# 选股函数
def check_stocks(context):
    #得到新能源指数成分股
    # g.stocks = get_index_stocks('399808.XSHE')
    # 半导体成分股
    g.stocks = get_index_stocks('931743.CSI')
    #查询股票市净率，并按照市净率升序排序
    if len(g.stocks) > 0:
        g.df = get_fundamentals(
                    query(valuation.code,valuation.pb_ratio)
                    .filter(valuation.code.in_(g.stocks))
                    # 获取市净率低的
                    # .order_by(valuation.pb_ratio.asc())
                    # 获取市净率高的
                    .order_by(valuation.pe_ratio.desc())
                )
        #筛选最低市净率的一只股票
        g.code = g.df['code'][0]
    
#交易函数
def trade(context):
    if len(g.stocks) > 0:
        code = g.code
    #若持仓股票不是最低市净率的股票，卖出
    for stock in context.portfolio.positions.keys():
        if stock != code:
            order_target(stock,0)
    #持仓股票
    if len(context.portfolio.positions) > 0:
        return
    else:
        order_value(code,context.portfolio.cash)
    
```



## 7.低估值量化交易策略
### 1.低估值量化交易策略介绍
:::info
**策略背景：**

股票净值是决定股票市场价格走向的主要根据。<font style="color:#DF2A3F;">市净率越低的股票，其投资价值越高;相反，其投资价值就越小</font>。但在判断投资价值时还要考虑<font style="color:#DF2A3F;">当时的市场环境以及公司经营情况、盈利能力</font>等因素

**策略算法：**

市净率小于1

负债比例低于于市场平均值

企业的流动资产至少是流动负债的1.2倍

每月一次调仓

可加入止损(十天沪深300跌幅达10%清仓)

:::



### 2.低估值量化交易策略实现思路
:::info
导入函数库，设定初始化函数

实现策略选股

实现止损函数

实现策略交易

:::



### 3.代码示例
```python
from jqdata import *
from jqlib.technical_analysis import *

# 初始化函数
def initialize(context):
    # 设定基准：沪深300
    set_benchmark('000300.XSHG')
    # 开启动态复权模式（真实价格）
    set_option('use_real_price', True)
    # 设定成交量比例
    set_option('order_volume_ratio', 1)
    
    # 股票交易手续费设置
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')
    
    # 最大持仓数量
    g.stocknum = 5
    # 选股指数：沪深300（必须定义！）
    g.stockindex = '000300.XSHG'
    # 自动设定调仓月份（每月调仓）
    f = 12
    g.Transfer_date = list(range(1, 13, 12 // f))
    
    # 每日开盘执行大盘止损
    run_daily(broader_stoploss, time='open')
    # 每月20号开盘调仓
    run_monthly(trade, monthday=20, time='open')

# 选股核心：低市净率 + 偿债能力强 + 低负债率
def check_stocks(context):
    # 获取指数成分股
    security = get_index_stocks(g.stockindex)
    
    # 财务筛选
    stocks = get_fundamentals(
        query(
            valuation.code,
            valuation.pb_ratio,
            balance.total_assets,
            balance.total_liability,
            balance.total_current_assets,
            balance.total_current_liability
        ).filter(
            valuation.code.in_(security),
            valuation.pb_ratio < 1,          # 市净率 < 1（破净股）
            (balance.total_current_assets / balance.total_current_liability) > 1.2  # 流动比率 > 1.2
        )
    )
    
    # 计算资产负债率（修复变量名错误）
    stocks['debt_asset'] = stocks['total_liability'] / stocks['total_assets']
    # 取负债率中位数
    debt_median = stocks['debt_asset'].median()
    # 筛选负债率低于中位数的股票
    codes = stocks[stocks['debt_asset'] < debt_median].code.tolist()
    
    return codes

# 大盘止损触发
def broader_stoploss(context):
    # 使用方法2：N日跌幅超过阈值则清仓
    stoploss = bm_stoploss(kernel=2, n=3, threshold=0.1)
    if stoploss:
        # 清空所有持仓
        for stock in list(context.portfolio.positions.keys()):
            order_target(stock, 0)
        log.info("大盘止损触发，已清空所有持仓")

# 大盘止损判断函数
def bm_stoploss(kernel=2, n=10, threshold=0.03):
    benchmark = '000300.XSHG'
    
    # 方法1：均线死叉止损
    if kernel == 1:
        t = n + 2
        hist = attribute_history(benchmark, t, '1d', 'close', df=False)
        ma1 = sum(hist['close'][1:-1]) / n
        ma2 = sum(hist['close'][0:-2]) / n
        close1 = hist['close'][-1]
        close2 = hist['close'][-2]
        return (close2 > ma2) and (close1 < ma1)
    
    # 方法2：N日跌幅止损（默认使用）
    elif kernel == 2:
        hist = attribute_history(benchmark, n, '1d', 'close', df=False)
        drop_rate = 1 - (hist['close'][-1] / hist['close'][0])
        return drop_rate >= threshold
    
    return False

# 交易调仓函数
def trade(context):
    current_month = context.current_dt.month
    
    # 只在设定月份调仓
    if current_month not in g.Transfer_date:
        return
    
    # 获取选股列表
    buylist = check_stocks(context)
    # 最多持仓数量
    hold_max = g.stocknum
    
    # ==================== 卖出逻辑 ====================
    for stock in list(context.portfolio.positions.keys()):
        if stock not in buylist:
            order_target(stock, 0)
            log.info(f"卖出不在选股池中的股票：{stock}")
    
    # ==================== 买入逻辑 ====================
    # 已持仓数量
    hold_num = len(context.portfolio.positions)
    need_buy_num = hold_max - hold_num
    
    if need_buy_num > 0 and len(buylist) > 0 and context.portfolio.cash > 1000:
        # 平均分配资金
        cash_per_stock = context.portfolio.cash / need_buy_num
        
        # 买入未持有的股票
        for stock in buylist:
            if stock not in context.portfolio.positions and need_buy_num > 0:
                order_value(stock, cash_per_stock)
                log.info(f"买入股票：{stock}，分配资金：{cash_per_stock:.2f}")
                need_buy_num -= 1
```



## 8.大小盘轮动量化交易策略
### 1.大小盘轮动量化交易策略介绍
:::info
**策略原理：**

策略来源国泰君安《20111110<font style="color:#DF2A3F;">风格轮动下的基金组合策略</font>》研报内容，尝试构建相<font style="color:#DF2A3F;">对强弱指标</font>(RS)并据此观察<font style="color:#DF2A3F;">风格持续性和利用方法</font>。



**RS指标构建：**

大盘风格代表：<font style="color:#DF2A3F;">沪深300</font>

小票风格代表：<font style="color:#DF2A3F;">创业板指数</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">RS指标算法：</font>**

<font style="color:#DF2A3F;">如图</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">指标判断：</font>**

<font style="color:#000000;">当RS指标大于0说明大盘风格强势，反之说明小盘风格强势</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">指标应用：</font>**

<font style="color:#000000;">RS指标分别求一阶导数、二阶导数;</font>

<font style="color:#DF2A3F;">一阶导数说明指标趋势，二阶导数说明趋势速度</font>

<font style="color:#DF2A3F;">一阶导数大于0，上涨，反之下跌</font>

<font style="color:#DF2A3F;">二阶导数大于0，加速，反之减速</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">投资标的：</font>**

<font style="color:#000000;">大盘投资标的：沪深300ETF</font>

<font style="color:#000000;">小盘投资标的：创业板ETF</font>

:::

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1779172376664-d979f38a-a915-47c7-8fbd-4861356efe03.png" width="429" title="" crop="0,0,1,1" id="uf786d313" class="ne-image">

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1779173395461-82b2c012-8f15-46a3-a453-6a944a23b820.png" width="916" title="" crop="0,0,1,1" id="uf427b576" class="ne-image">



**大小盘量化交易策略信号识别**

<img src="https://cdn.nlark.com/yuque/0/2026/png/21971555/1779173577076-47c77de5-dd8e-484a-b4b8-3adc82cc3940.png" width="1243" title="" crop="0,0,1,1" id="u16205ccc" class="ne-image">





### 2.大小盘轮动量化交易策略实现思路
:::info
1、导入函数库，设定策略基础参数

2、设定初始化函数:

3、实现策略信号识别

4、实现策略交易

:::



### 3.代码示例
```python
# 大小盘轮动量化交易策略
from jqdata import *
from datetime import datetime, timedelta
import math
import pandas as pd
import statsmodels.api as sm
import numpy as np

# 设定基础参数
strBig = '000300.XSHG'       # 沪深300
strSmall = '399006.XSHE'     # 创业板指
strMarket = '000047.XSHG'    # 全市场指数
index = [strBig, strSmall, strMarket]
etfBig = '510300.XSHG'       # 沪深300ETF
etfSmall = '159915.XSHE'     # 创业板ETF
g.result = {etfBig: 0, etfSmall: 0}

# 初始化函数
def initialize(context):
    # 设定基准：沪深300
    set_benchmark('000300.XSHG')
    # 开启动态复权模式（真实价格）
    set_option('use_real_price', True)
    
    # 股票交易手续费设置
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        close_today_commission=0,
        min_commission=5
    ), type='stock')

    run_monthly(market_open, monthday=1)

# 计算交易信号
def get_signal(tradeDate):
    start_date = datetime.strptime(tradeDate, '%Y-%m-%d') - timedelta(days=1000)
    start_date = start_date.strftime('%Y-%m-%d')
    # 获取数据
    data = get_price(index,
                    start_date=start_date,
                    end_date=tradeDate,
                    frequency='daily',
                    fields='close',
                    fq='pre')['close']
                    
    data = data / data.shift(250)
    data.dropna(inplace=True)
    
    # 计算RS指标
    for c in data.columns:
        if c != strMarket:
            data[c] = data[c] - data[strMarket] + 1
    data = data.drop(strMarket, axis=1)
    
    # 对数处理
    for c in data.columns:
        data[c] = data[c].apply(lambda x : math.log(x, 10))
        
    # 计算RS的HP滤波
    diff = data[strBig] - data[strSmall]
    cycle, trend = sm.tsa.filters.hpfilter(diff, lamb=10000)
    
    # 计算前20个数据一阶及二阶导数
    t1 = []
    for pos in range(-20, 0):
        X = np.arange(20)
        X = sm.add_constant(X)
        y = trend.iloc[pos - 20 : pos]
        est = sm.OLS(y, X).fit()
        t1.append(est.params[1])
    
    # 计算二阶导数
    X = np.arange(20)
    X = sm.add_constant(X)
    est1 = sm.OLS(t1, X).fit()
    t2 = est1.params[1]
    result = {}
    
    # 通过四象限结果计算持仓比例
    if t1[-1] > 0 and t2 > 0:
        result[etfBig] = 1
        result[etfSmall] = 0
    elif t1[-1] > 0 and t2 < 0:
        result[etfBig] = 0.5
        result[etfSmall] = 0.5
    elif t1[-1] < 0 and t2 > 0:
        result[etfBig] = 0.5
        result[etfSmall] = 0.5
    elif t1[-1] < 0 and t2 < 0:
        result[etfBig] = 0
        result[etfSmall] = 1
    return result

# 交易函数，开盘时运行
def market_open(context):
    result = get_signal(context.previous_date.strftime('%Y-%m-%d'))
    # 修复：etfBigl → etfBig 拼写错误；括号匹配
    if not (g.result[etfBig] == result[etfBig] and g.result[etfSmall] == result[etfSmall]):
        # 先清仓
        order_target_value(etfBig, 0)
        order_target_value(etfSmall, 0)
        
        # 根据现金买入指定比例etf
        cash = context.portfolio.available_cash
        order_target_value(etfBig, result[etfBig] * cash)
        order_target_value(etfSmall, result[etfSmall] * cash)
        
        # 更新全局持仓记录
        g.result = result
        

```



## 9.逆三因子量化交易策略
### 1.三因子量化交易策略介绍
:::info
**三因子策略：**

即Fama-French三因子模型，<font style="color:#DF2A3F;">Fama</font>和<font style="color:#DF2A3F;">French</font> 1992年对美国股票市场决定不同股票回报率差异的因素的研究发现，<font style="color:#DF2A3F;">股票的市场的beta值不能解释不同股票回报率的差异，而上市公司的市值、账面市值比、市盈率可以解释股票回报率的差异。</font>Fama and French认为，上述超额收益是对CAPM 中β未能反映的风险因素的补偿。



**三因子火锅，既美味又营养**

市场风险、市值风险、B/M风险



三因子模型的作用，<font style="color:#DF2A3F;">在于发现了股票的期望收益不仅仅与市场的系统风险有关，还和市值风险和账面市值比风险有关。</font>

<font style="color:#DF2A3F;"></font>

**<font style="color:#000000;">市场风险因子：</font>**

市场回报(沪深300的日度收益率)减去无风险收益率(国债的日度收益率)

**市值因子：**

公司的总市值的自然对数

**账面市值比因子：**

最新一季财报的账面价值与当前市值的比值(pb_ratio的倒数)



**传统三因子策略价值：**

<font style="color:#DF2A3F;">小市值的公司的股票平均收益率更高</font>

<font style="color:#DF2A3F;">市净率(M/E)率低的公司的平均收益更高</font>



**传统三因子策略不足：**

并没有找到两个因子很好的解释市值溢价和价值溢价在A股市场2016年之后的表现不好



**逆三因子策略：**

采用反向指标替换传统三因子模型。用<font style="color:#DF2A3F;">VROC12</font>、<font style="color:#DF2A3F;">Residual Volatility</font>和<font style="color:#DF2A3F;">Size</font>三个因子构建Zscore，每月取Zscore最低的50支股票建立多头头寸。



**逆三因子-特质因子：**

Residual Volatility，残差波动率因子，又称特质因子。<font style="color:#DF2A3F;">Barra模型中衡量市场中不能解释的信息数据的波动情况</font>。在A股中效果显著

****

**逆三因子-市值因子：**

使用Size因子，即市值规模的因子。根据研报及经验分析，<font style="color:#DF2A3F;">A股市场市值因子效应是存在的，小市值股票收益率更高</font>。量的差异计算

****

**逆三因子-情绪因子：**

VROC12，即情绪因子，通过近期交易量和N日前平均交易

:::



### 2.逆向三因子量化交易策略介绍
:::info
**选股策略：**

包含所有A股股票，过滤ST股票



**策略信号：**

每个月第一个交易日前，挑选出市值、特质因子、情绪因子最低(三个指标等权重平均计算Z-Score)的50支股票



**交易方式：**

等权持仓

:::



### 3.逆向三因子量化交易策略实现思路
:::info
1、导入函数库，设定初始化函数

2、实现策略信号识别版

3、实现策略交易

4、打印每日成交记录

:::



### 4.代码示例
```python
# 导入聚宽必备库
import pandas as pd
import numpy as np
from jqdata import *

# ===================== 策略初始化配置 =====================
def initialize(context):
    # 基准：沪深300
    set_benchmark('000300.XSHG')
    # 真实复权价格
    set_option('use_real_price', True)
    # 交易成本
    set_order_cost(OrderCost(
        open_tax=0,
        close_tax=0.001,
        open_commission=0.0003,
        close_commission=0.0003,
        min_commission=5
    ), type='stock')
    # 滑点（新版必须用FixedSlippage）
    set_slippage(FixedSlippage(0.001))

    # 策略参数
    g.stock_num = 50    # 选50只
    g.month = None      # 控制每月只调一次

# ===================== 核心选股 =====================
def get_target_stocks(context):
    # 1. 全A股列表
    all_stocks = get_all_securities(types=['stock'], date=context.current_dt)
    stock_list = all_stocks.index.tolist()

    # 2. 过滤ST + 停牌 + 上市不足60天（已修复时间类型错误）
    current_data = get_current_data()
    today_date = context.current_dt.date()  # 转成date类型
    
    stock_list = [
        stock for stock in stock_list
        if not current_data[stock].is_st       # 非ST/*ST
        and not current_data[stock].paused     # 非停牌
        and (today_date - all_stocks.loc[stock, 'start_date']).days >= 60
    ]

    if len(stock_list) == 0:
        return []

    # 3. 取因子数据：市值、换手率
    q = query(
        valuation.code,
        valuation.market_cap,        # 市值因子
        valuation.turnover_ratio     # 情绪因子（换手率）
    ).filter(
        valuation.code.in_(stock_list)
    )
    df = get_fundamentals(q, date=context.current_dt)

    # 4. 计算特质波动率（近20日）
    def get_iv(code):
        try:
            # 股票收益
            ret = get_price(code, end_date=context.current_dt, count=20, fields='close')['close'].pct_change().dropna()
            # 市场收益（沪深300）
            bench = get_price('000300.XSHG', end_date=context.current_dt, count=20, fields='close')['close'].pct_change().dropna()
            # 回归取残差波动率
            beta = np.cov(ret, bench)[0][1] / np.var(bench)
            res = ret - beta * bench
            return np.std(res)
        except:
            return np.nan

    df['iv'] = df['code'].apply(get_iv)
    df = df.dropna()

    if len(df) < g.stock_num:
        return []

    # 5. Z-Score标准化（等权重）
    for col in ['market_cap', 'iv', 'turnover_ratio']:
        mean = df[col].mean()
        std = df[col].std()
        df[f'{col}_z'] = (df[col] - mean) / std

    # 逆向三因子综合分（越小越好）
    df['score'] = (df['market_cap_z'] + df['iv_z'] + df['turnover_ratio_z']) / 3

    # 6. 取分数最低的50只
    df = df.sort_values('score', ascending=True)
    target_list = df.head(g.stock_num)['code'].tolist()

    return target_list

# ===================== 每月调仓 =====================
def before_trading_start(context):
    # 每月第一个交易日执行
    today_month = context.current_dt.month
    if today_month == g.month:
        return
    g.month = today_month

    target_stocks = get_target_stocks(context)
    if not target_stocks:
        return

    # 卖出不在目标池的
    for stock in context.portfolio.positions:
        if stock not in target_stocks:
            order_target_value(stock, 0)

    # 等权重买入
    cash = context.portfolio.available_cash
    per_cash = cash / len(target_stocks)
    for stock in target_stocks:
        order_target_value(stock, per_cash)

# ===================== 盘后日志 =====================
def after_market_close(context):
    log.info(f'持仓数量: {len(context.portfolio.positions)}')
```


































