# $C' = (-1)^{L+S}$ 的推导

## 1. 物理系统与记号

考虑一对正反粒子 $A\bar A$ 的束缚态或散射态，在质心系中：

- 轨道角动量：$L$
- 单个粒子的自旋：$s$
- 总自旋：$S$
- 总角动量：$J$

在质心系中，可用相对坐标 $\vec r$ 表示两粒子的空间自由度，用 $(s_1,s_2)$ 表示两粒子的自旋取值。态矢量可写成（略去规范化等因子）：
$$
\Psi_{LSJM}(\vec r,s_1,s_2)
= R_{L}(r)\,Y_{LM_L}(\hat r)\,\chi_{SM_S}(s_1,s_2)
$$
其中 $Y_{LM_L}$ 是球谐函数，$\chi_{SM_S}$ 是两粒子自旋总角动量为 $S$ 的自旋波函数。

---

## 2. $P$ 变换与 $P'$ 的计算

### 2.1 空间部分

空间反演变换 $P$：
$$
P:\quad \vec r \to -\vec r
$$

球谐函数的性质：
$$
Y_{LM_L}(-\hat r) = (-1)^L Y_{LM_L}(\hat r)
$$

因此空间波函数在 $P$ 变换下得到一个因子 $(-1)^L$。

### 2.2 本征宇称与正反粒子

设粒子 $A$ 的本征宇称为 $\eta_A$，则反粒子 $\bar A$ 的本征宇称为
$$
\eta_{\bar A} = (-1)^{2s}\,\eta_A
$$
（这是相对论量子场论中的标准结果：粒子与反粒子的本征宇称相差 $(-1)^{2s}$）。

于是 $A\bar A$ 体系在 $P$ 下的本征值为
$$
P' = \eta_A\eta_{\bar A}(-1)^L
   = \eta_A^2(-1)^{2s}(-1)^L
$$

由于整体相位无物理意义，可重新定义场的相位使得 $\eta_A^2 = 1$，从而得到
$$
\boxed{P' = (-1)^{L+2s}}
$$

常用的两个特例：

- 正反**费米子对**（如 $e^+e^-$）：$s=\tfrac12$  
  $$
  P' = (-1)^{L+1}
  $$
- 正反**玻色子对**（如标量介子对）：$s$ 为整数  
  $$
  P' = (-1)^L
  $$

---

## 3. $CP$ 作用在 $A\bar A$ 态上的详细推导

### 3.1 用坐标和自旋标记的态

先用“粒子在 $\vec r$，反粒子在 $-\vec r$”的记号写态：
$$
\bigl|\Psi_{LS}(\vec r;s_1,s_2)\bigr\rangle
\ \equiv\ \bigl|A(\vec r,s_1)\,\bar A(-\vec r,s_2)\bigr\rangle
$$

### 3.2 先做 $P$ 再做 $C$

1. **$P$ 作用：**

对空间坐标：
$$
P:\quad \vec r \to -\vec r,\qquad -\vec r \to \vec r
$$

于是
$$
P\,\bigl|A(\vec r,s_1)\,\bar A(-\vec r,s_2)\bigr\rangle
= \eta_A\eta_{\bar A}(-1)^L
  \bigl|A(-\vec r,s_1)\,\bar A(\vec r,s_2)\bigr\rangle
$$
这里 $(-1)^L$ 来自空间波函数的球谐部分。

2. **$C$ 作用：**

$C$ 把粒子变成反粒子、反粒子变成粒子。设
$$
C\,|A(\vec x,s)\rangle = \xi_A\,|\bar A(\vec x,s)\rangle,\qquad
C\,|\bar A(\vec x,s)\rangle = \xi_{\bar A}\,|A(\vec x,s)\rangle
$$
其中 $\xi_A,\xi_{\bar A}$ 是模为 1 的相位。对两粒子态有
$$
\begin{aligned}
C\,\bigl|A(-\vec r,s_1)\,\bar A(\vec r,s_2)\bigr\rangle
&= \xi_A\xi_{\bar A}\,
   \bigl|\bar A(-\vec r,s_1)\,A(\vec r,s_2)\bigr\rangle \\
&= \xi_A\xi_{\bar A}\,
   \bigl|A(\vec r,s_2)\,\bar A(-\vec r,s_1)\bigr\rangle
\end{aligned}
$$
最后一步只是把粒子与反粒子的**标记顺序对调**（这是一个“交换算符”，只影响自旋波函数的对称性，不改变空间坐标的相对取向）。

综合两步：
$$
CP\,\bigl|A(\vec r,s_1)\,\bar A(-\vec r,s_2)\bigr\rangle
= \eta_A\eta_{\bar A}\xi_A\xi_{\bar A}(-1)^L
   \bigl|A(\vec r,s_2)\,\bar A(-\vec r,s_1)\bigr\rangle
$$

同样可以通过重新定义场的整体相位，使得
$$
\eta_A\eta_{\bar A}\xi_A\xi_{\bar A} = 1
$$
于是
$$
\boxed{CP:\quad
\bigl|\Psi_{LS}(\vec r;s_1,s_2)\bigr\rangle
\ \longrightarrow\
(-1)^L\,\bigl|\Psi_{LS}(\vec r;s_2,s_1)\bigr\rangle}
$$

我们可以将其理解为：**$CP$ 的作用 = 空间给出 $(-1)^L$，再把两个粒子的自旋指标交换。**

---

## 4. 自旋波函数在交换下的对称性

上面看到 $CP$ 的效果只剩下两个操作：

1. 乘上空间因子 $(-1)^L$；
2. 对自旋波函数做一次“交换 $(s_1\leftrightarrow s_2)$”。

因此关键是：**总自旋为 $S$ 的两粒子自旋波函数，在交换两粒子时的本征值是多少？**

### 4.1 两个费米子（以 $s=\tfrac12$ 为例）

以两电子的自旋为例，总自旋可以是 $S=0$ 或 $S=1$。显式写出自旋态：

- $S=1$ 三重态（对称）：
  $$
  \begin{aligned}
  |1,1\rangle &= |\uparrow\uparrow\rangle \\
  |1,0\rangle &= \frac{1}{\sqrt2}\bigl(|\uparrow\downarrow\rangle
                                     + |\downarrow\uparrow\rangle\bigr) \\
  |1,-1\rangle&= |\downarrow\downarrow\rangle
  \end{aligned}
  $$
  对交换算符 $P_{12}$：
  $$
  P_{12}|1,m\rangle = +\,|1,m\rangle
  $$

- $S=0$ 单重态（反对称）：
  $$
  |0,0\rangle = \frac{1}{\sqrt2}\bigl(|\uparrow\downarrow\rangle
                                   - |\downarrow\uparrow\rangle\bigr)
  $$
  对交换算符：
  $$
  P_{12}|0,0\rangle = -\,|0,0\rangle
  $$

总结：两费米子自旋波函数在交换下的本征值为
$$
P_{12}\chi_{SM_S}^{(f)} = 
\begin{cases}
+\,\chi_{SM_S}^{(f)}, & S=1 \\
-\,\chi_{SM_S}^{(f)}, & S=0
\end{cases}
$$
这可以写成统一的形式：
$$
\boxed{P_{12}\chi_{SM_S}^{(f)} = (-1)^{S+1}\chi_{SM_S}^{(f)}}
$$

一般自旋为 $s=\tfrac12$ 的正反费米子对也是如此：$S$ 为奇数时自旋波函数在交换下对称，为偶数时反对称，对应因子 $(-1)^{S+1}$。

### 4.2 两个玻色子（如两矢量玻色子）

以两自旋 1 玻色子的例子为代表，总自旋可以取 $S=0,1,2$。显式构造可验证：

- $S=0$ 与 $S=2$ 的自旋波函数在交换下是**对称**的；
- $S=1$ 的自旋波函数在交换下是**反对称**的。

因此：
$$
P_{12}\chi_{SM_S}^{(b)} =
\begin{cases}
+\,\chi_{SM_S}^{(b)}, & S=0,2,\dots \ (\text{偶 }S) \\
-\,\chi_{SM_S}^{(b)}, & S=1,3,\dots \ (\text{奇 }S)
\end{cases}
$$
可以写成统一形式：
$$
\boxed{P_{12}\chi_{SM_S}^{(b)} = (-1)^{S}\chi_{SM_S}^{(b)}}
$$

---

## 5. $CP$ 的特征值 $(CP)'$

把第 3 节得到的 $CP$ 作用式
$$
CP:\quad
\Psi_{LS}(\vec r;s_1,s_2)
\ \longrightarrow\
(-1)^L\,\Psi_{LS}(\vec r;s_2,s_1)
$$
与本节的自旋交换性质结合：

- 对**正反费米子对**：
  $$
  \Psi_{LS}(\vec r;s_2,s_1)
  = (-1)^{S+1}\Psi_{LS}(\vec r;s_1,s_2)
  $$
  故
  $$
  CP\,|\Psi_{LS}\rangle
  = (-1)^L\,(-1)^{S+1}|\Psi_{LS}\rangle
  $$
  即
  $$
  \boxed{(CP)'_{\text{费}} = (-1)^{L+S+1}}
  $$

- 对**正反玻色子对**：
  $$
  \Psi_{LS}(\vec r;s_2,s_1)
  = (-1)^S\Psi_{LS}(\vec r;s_1,s_2)
  $$
  故
  $$
  CP\,|\Psi_{LS}\rangle
  = (-1)^L\,(-1)^S|\Psi_{LS}\rangle
  $$
  即
  $$
  \boxed{(CP)'_{\text{玻}} = (-1)^{L+S}}
  $$

不过我们更关心的是**仅 $C$ 的本征值 $C'$**，而不是 $CP$。注意
$$
(CP)' = C'P'
$$
因此可以用已知的 $P'$ 来求得 $C'$。

---

## 6. 用 $P'$ 与 $(CP)'$ 求 $C'$：得到 $C' = (-1)^{L+S}$

### 6.1 正反费米子对

- 上面得到：
  $$
  P'_{\text{费}} = (-1)^{L+1},\qquad
  (CP)'_{\text{费}} = (-1)^{L+S+1}
  $$
- 于是：
  $$
  C'_{\text{费}}
  = \frac{(CP)'_{\text{费}}}{P'_{\text{费}}}
  = \frac{(-1)^{L+S+1}}{(-1)^{L+1}}
  = (-1)^{L+S}
  $$

### 6.2 正反玻色子对

- 上面得到：
  $$
  P'_{\text{玻}} = (-1)^L,\qquad
  (CP)'_{\text{玻}} = (-1)^{L+S}
  $$
- 因此：
  $$
  C'_{\text{玻}}
  = \frac{(CP)'_{\text{玻}}}{P'_{\text{玻}}}
  = \frac{(-1)^{L+S}}{(-1)^L}
  = (-1)^{L+S}
  $$

于是，对**正反费米子对和正反玻色子对**，我们都得到统一的结果：
$$
\boxed{C'_{A\bar A} = (-1)^{L+S}}
$$

---

## 7. 总结

- $P'$ 只依赖于轨道角动量 $L$ 和单粒子自旋 $s$：
  $$
  P' = (-1)^{L+2s}
  $$
- $C'$ 则依赖于 $L$ 与总自旋 $S$：
  $$
  C' = (-1)^{L+S}
  $$
- 直观理解：
  - $L$ 控制空间波函数在反演/交换下的对称性；
  - $S$ 控制自旋波函数在交换下的对称性；
  - 对正反粒子体系，$C$ 变换本质上等价于“空间反演 + 交换”，故指数为 $L+S$。

在粒子谱和强子态的量子数分析中，这个结果被广泛使用。
