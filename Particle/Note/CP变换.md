# 1.CP变换定义和性质
同时作用CP有两种顺序选择：
$$
	CP\ket{A} \text{or}PC\ket{A} 
$$
一般情况下，正反粒子p宇称不一定相等，CP并不对易，也没有共同本征态，除了纯中性系统。
$$
	\begin{align}
		CP\ket{A} = CP^{'}(A)\ket{A} = C^{'}P^{'}(\bar{A})\ket{A}  \\
		PC\ket{A} = PC^{'}(A)\ket{\bar{A}} = P^{'}(\bar{A})C^{'}\ket{\bar{A}}  
	\end{align}
$$
**CP变换的性质**
1. 纯中性粒子的CP宇称为二者乘积。
2. 正反粒子组成的纯中性系统本征值为$(-1)^{S+2s}$，$\color{red}和轨道角动量无关$。
	这个结论可以由之前的结论推得，对正反粒子系统：
	- P宇称为$(-1)^{L+2s}$
	- C宇称为$(-1)^{L+S}$
	相乘即得。
3. 两个CP本征态构成的系统：$CP^{'}(AB) = CP^{'}(A)CP^{'}(B)(-1)^{L}$

# 2.弱相互作用的CP不变性
**CP变换不变性**
- 定义：通过CP变换联系的两个过程，其演化性质和概率分布完全相同。

**弱相互作用中的例子**
- 过程：$\pi^{+}\rightarrow\mu^{+}\nu_{\mu}$ 与 $\pi^{-}\rightarrow\mu^{-}\bar{\nu}_{\mu}$ 通过CP变换相互联系：
  - $\pi^{+}(\vec{p})\overset{CP}{\rightarrow}\pi^{-}(-\vec{p})$
  - $\mu^{+}(\vec{k},s_{k})\overset{CP}{\rightarrow}\mu^{-}(-\vec{k},s_{k})$
  - $\nu_{\mu}(\vec{k}^{\prime},s_{k^{\prime}}\!=\!-\frac{1}{2})\overset{CP}{\rightarrow}\bar{\nu}_{\mu}(-\vec{k}^{\prime},s_{k^{\prime}}\!=\!-\frac{1}{2})$

**结论**：CP不变性要求两过程的衰变宽度完全相同，实验已验证。 
# 3.CP破坏
$K^{0}$和其反粒子$\bar{K}^0$的奇异数和同位旋第三分量不同，但是弱相互作用下这两个差异不是守恒量，不能用这两个守恒量判断粒子衰变行为。但是会发现，一部分中性K介子衰变慢$K_L$，一部分衰变得快$K_S$，由此做出以下分析步骤
1. 利用CP不变性
	其实弱相互作用下由微弱的CP破坏，但是我们先将其忽略。把K介子衰变速度不同的原因归结为，这两部分CP宇称不同。
	- 弱相互作用中CP变换近似不变，K⁰与反K⁰形成CP本征态的叠加：
		$$
		\begin{aligned}
		|K_{S}\rangle &= \frac{1}{\sqrt{2}}(|K^{0}\rangle +CP |\bar{K}^{0}\rangle)= \frac{1}{\sqrt{2}}(|K^{0}\rangle - |\bar{K}^{0}\rangle), \quad CP|K_S\rangle = +|K_S\rangle \\
		|K_{L}\rangle &= \frac{1}{\sqrt{2}}(|K^{0}\rangle -CP |\bar{K}^{0}\rangle)= \frac{1}{\sqrt{2}}(|K^{0}\rangle + |\bar{K}^{0}\rangle), \quad CP|K_L\rangle = -|K_L\rangle
		\end{aligned}
		$$
	类似一个奇偶分解。
	- ππ系统CP=+1，$K_S$→ππ允许（主衰变，相空间大，寿命短）
	- $K_L$→ππ禁戒，只能衰变到3π（相空间小，寿命长）
2. 再论CP破坏
	1. 1946年发现了$K_L$到$\pi\pi$的衰变，这表明在若相互作用中有CP破坏的分量。
	2. 如果考虑CP破坏效应，快慢态可以修正为：
$$
\begin{aligned}
|K_{S}\rangle &= \frac{1}{\sqrt{2(1+|\varepsilon|^{2})}} \left[ (1+\varepsilon)|K^{0}\rangle + (1-\varepsilon)CP|K^{0}\rangle \right], \\
|K_{L}\rangle &= \frac{1}{\sqrt{2(1+|\varepsilon|^{2})}} \left[ (1+\varepsilon)|K^{0}\rangle - (1-\varepsilon)CP|K^{0}\rangle \right].
\end{aligned}
$$
3. 进一步讨论正反中性K介子系统
	- 正反中性K介子系统的CP宇称（不考虑CP破坏）
		$K_s$和$K_L$都是CP变换的本征态，这样可以得到
		$$
			\begin{align}
					CP(K_SK_L) = CP(K_S)CP(K_L)(-1)^L \\
					CP(K_SK_S) = CP(K_S)CP(K_S)(-1)^L \\
					CP(K_LK_L) = CP(K_L)CP(K_L)(-1)^L \\
			\end{align}
		$$


**CP破坏“可能”的来源**
1. 强CP破坏
	QCD理论的拉格朗日量中有一项$\mathcal{L}_\theta = \theta\frac{g^2}{32\pi^2}TrF_{\mu\nu}\widetilde{F}^{\mu \nu}$，$\theta$无量纲其不为0将导致CP破坏。弱实验上发现CP破坏源于此，则其值应该为$10^{-8}$。
2. 弱CP破坏
	不同代的夸克之间存在混合，其混合矩阵是：
	CKM矩阵是一个幺正矩阵，其参数化是三个欧拉角和一个不可去的相角，这个相角会破坏CP。
-  CP破坏也是宇宙物质-反物质不对称的可能来源。

# 4.CPT定理
**CPT定理：** 如果
- 所讨论的场是$\color{red}定域场$；
- 场具有$\color{blue}正洛伦兹不变性$
- 满足$\color{blue}自旋统计关系$
则运动定律再联合变换下不变。

**推论：**
- 粒子和反粒子的质量、寿命、自旋磁矩的g因子都完全相同。
- 粒子的$\color{blue}某一衰变道$的衰变速率和C变换后反粒子的相应衰变道衰变速率$\color{blue}不一定相等$，除非C宇称守恒。

**细致平衡原理：** 源自时间反演不变性，反应的正、逆进行时的跃迁振幅相等。
可以类比Feynman图，拓扑结构中扭动外线得到的结果不变，物理意义上进行了时间的反演。

**T破坏**：弱作用下CP不守恒，那CPT守恒应该可以得到T变换不守恒。
