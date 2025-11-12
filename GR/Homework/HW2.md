# 作业

## 1. 2-球面的度量、Christoffel 符号与 Ricci 张量

给定二维球面（取半径 $r=1$）的坐标 $(\theta,\phi)$，度规为  
$$
ds^2 = d\theta^2 + \sin^2\theta\, d\phi^2, \qquad
(g_{\mu\nu})=\mathrm{diag}(1,\ \sin^2\theta),\quad
(g^{\mu\nu})=\mathrm{diag}(1,\ \csc^2\theta).
$$

由  
$$
\Gamma^\rho_{\mu\nu}=\tfrac12 g^{\rho\sigma}
(\partial_\mu g_{\sigma\nu}+\partial_\nu g_{\sigma\mu}-\partial_\sigma g_{\mu\nu})
$$
可得该坐标系下唯一非零的 Christoffel 符号：  
$$
\Gamma^{\theta}_{\phi\phi}=-\sin\theta\cos\theta,\qquad
\Gamma^{\phi}_{\theta\phi}=\Gamma^{\phi}_{\phi\theta}=\cot\theta.
$$

Riemann → Ricci 取缩并  
$$
R_{\mu\nu}
=\partial_\lambda \Gamma^\lambda_{\mu\nu}
-\partial_\nu \Gamma^\lambda_{\mu\lambda}
+\Gamma^\lambda_{\mu\nu}\Gamma^\sigma_{\lambda\sigma}
-\Gamma^\sigma_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}.
$$

代入上式并化简（用恒等式 $\csc^2\theta-\cot^2\theta=1$），得  
$$
R_{\theta\theta}=1,\qquad
R_{\phi\phi}=\sin^2\theta,\qquad
R_{\theta\phi}=0.
$$

进一步有标量曲率  
$$
R=g^{\mu\nu}R_{\mu\nu}=2.
$$


## 2. 里奇张量是黎曼张量的缩并

由黎曼张量定义  
$$
R^\rho{}_{\sigma\mu\nu}
=\partial_\mu\Gamma^\rho_{\nu\sigma}
-\partial_\nu\Gamma^\rho_{\mu\sigma}
+\Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma}
-\Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma},
$$

对第一、三指标做缩并得  
$$
R_{\mu\nu}
=R^\rho{}_{\mu\rho\nu}
=g^{\rho\sigma}R_{\rho\mu\sigma\nu}.
$$
（证毕）


## 3. 证明 $\nabla_\rho \delta^\mu{}_\nu=0$ 与 $\nabla_\rho g^{\mu\nu}=0$

首先  
$$
\nabla_\rho \delta^\mu{}_\nu
=\partial_\rho \delta^\mu{}_\nu
+\Gamma^\mu_{\rho\lambda}\delta^\lambda{}_\nu
-\Gamma^\lambda_{\rho\nu}\delta^\mu{}_\lambda
=\Gamma^\mu_{\rho\nu}-\Gamma^\mu_{\rho\nu}=0.
$$

对度量（Levi-Civita 联络）有度量相容性：  
$$
\nabla_\rho g^{\mu\nu}
=\partial_\rho g^{\mu\nu}
+\Gamma^\mu_{\rho\lambda}g^{\lambda\nu}
+\Gamma^\nu_{\rho\lambda}g^{\mu\lambda}
=0.
$$
（证毕）


## 4. 升降指标与协变导数的相容性

对任意 $(1,1)$ 型张量 $H^\mu{}_\nu$：  
$$
\nabla_\rho H^\mu{}_\nu
=\partial_\rho H^\mu{}_\nu
+\Gamma^\mu_{\rho\lambda}H^\lambda{}_\nu
-\Gamma^\lambda_{\rho\nu}H^\mu{}_\lambda.
$$

若 $\nabla_\rho g_{\mu\nu}=0$，则升/降指标与协变导数可交换：  
$$
\nabla_\rho H^{\mu\nu}
=g^{\nu\lambda}\nabla_\rho H^\mu{}_\lambda,\qquad
\nabla_\rho H_{\mu\nu}
=g_{\mu\lambda}\nabla_\rho H^\lambda{}_\nu.
$$
（证毕）
