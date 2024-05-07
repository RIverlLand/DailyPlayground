量产车：
国外代表的 特斯拉 FFD 12.0.3 纯视觉，端到端（传统智驾是：感知（视觉，点云，毫米波，4D毫米波雷达）-，新颖，
L2 ++
纯OA？

Adas：L0-L2，可能到不了L3 L4。
Adas: Advanced driving assistance system
OTA: Over the air
SOTA: Software over the air
FOTA: Firmware over the air
ALC: Automotive Lane Change
APA: Auto parking assist
FSD: Full self driving
ACC: Adaptive Cruise Control
AEB: Autonomous Emergency Braking
LKA: Lane Keeping Assist
EEA: Electrical/Electronic Architecture
电子控制单元(ECU)
拓扑图: Topological graph
SOP: Standard Operating Procedure
CAN: Controller Area Network
VRU：Vulnerable Road Users


1. Create, manage and steer testing and validation processes for the L2 driver assistance development projects.
   - L2:驾驶操作是车辆，但是人要监管；巡航、跟车、APA泊车、城市NOA（Navigate on Autopilot）之类的；
   - 根据项目进行测试：比如AEB,ACC,LKA各个，独立进行功能测试；可以是function导向的也可以是场景导向的
   - 大概流程：整车的E/E开发中，有个klausur team：周期性的软件更新、比如三个月一个大版本，每段时间一个sprint，每个sprint就会有一个窗口期，交付软件；由klausur的人刷软件到车上去测试，反馈问题，在接下来的sprint里做修复；最终的release中定下来一个表现好的sprint的状态，作为整车版本的release。**大众的体系里叫做VR，Verbund release**
   - 每个VR release之后会进行长周期的测试，比如冬测或者夏测；是不是最终进入SOP的才会测试还是很多都会测试就不清楚。
   - 比如大众sprint是两周，一个VR是三个sprint，所以基本VR是1.5个月，但不是每个VR都会做工业化，可能三个VR才做一个工业化，让供应商来做最终的更改。
   - 比如一个新车型实装，定在五月，不会去改sprint的时间，而是根据装车节点去选取哪个sprint作为装车的状态。
2. Design test scenario and test cases, maintain the test cases accroding to the requirements changes.
3. Collaborate with the component, system and function developers of for requirement break-down.
   1. component: 主管是比如奔驰的BTV；component是负责硬件区的，比如谁负责相机。。。比如空调：谁管压缩机，出风口；又比如body controller的硬件是简单的，system的owner就很复杂，E\E system owner（电子电气）或者speaker才能解决一些细节的问题，比如为什么尾灯不亮了
   2. system: 是系统？基本是搞软件的，对于功能的控制逻辑比较清楚。比如谁负责空调的软件，涉及到很多sensor，阀门，
      1. 行车域和泊车域（域控制就是功能区分的，比如智驾域、泊车域）
      2. 域控制器（和架构相关）：分布式、耦合式还是什么
         1. 座舱域是用来车机的控制，
         2. 智驾域是包含车外摄像头、雷达、域控制器等部分集成，和座舱通讯等等；查查GMSL接口？Can信号？
         3. 车身、地盘、信息娱乐、adas、链接域，基本是通过功能区分的
   3. function: 第一点中的？
4. Ensure the traceability between the requirements and test catalogue.
   1. 测试的问题需要能够重现
5. Use testing equipment (Vector, ODIS,..) to Reproduce the customer complaints and record traces.
   1. Vector：是个德国品牌，软件是CanOE，用来做Can总线上的全套工具链？总线的仿真，信号的截取分析编程blablabla（CAN总线上，信号表现为电压形式，通过CAN_H和CAN_L线上的电位差来表示CAN信号）；录一录trace，总线的报文；
      1. CANoe不仅限于CAN类型的总线开发，还包含LIN、FlexRay、MOST和以太网等开发。
      2. 报文(message)：can总线的数据是有很多位，起始、仲裁(acknowledgment bits)、数据、校验、帧结束之类的，组成了一个PDU；但是由于电瓶位不稳定，会有很多校验位
   2. ODIS：大众自己的诊断工具（通过OBD去车子的诊断界面,OBD是主控下的一个接口？）
6. Ability to conduct pre-analysis to locate the root-cause.
7. Track the bug-fix process, coordinate the JVs and Supplier to ensure quick and effective bug-fixing
   1. JVs：合资公司
8. Fleet-management, partially support on testing fleet management and test route plan
   1. 管车，一般上车跑的是三方测试公司
   2. 协调车的改造，提需求，下工单，管车的状态，测试目标
   3. function list 在大众叫Fuli = function list
9.  Knowledge in OEM development process and overall vehicle architecture
    1.  白车身的造型、blablabla，和我们没关系
    2.  每个车都是在一个平台上开发的，比如后驱，四驱，前驱，这样不同的设计可以沿用电气、设计等等
    3.  还会有扩展车，延申车型，比如领克01 05，就是同一车型的不同style
        1.  E3 2.0 是 SSP平台 (Scalable Systems Platform)
            1.  目前来看，大众已经在规划未来的软件平台复用了，对MEB、PPE平台上的软件架构的演化往更有效率的方向。大众在进行中的主要有三种电子电气架构，
              E³1.1 首先解决的问题是OTA无线升级和更新
              2023 年，CARIAD 将推出高级软件平台 1.2 (E³1.2)，这里主要革新的还是智能座舱和自动驾驶的功能，
              2025 年，CARIAD 的将可扩展的软件平台和电子架构2.0 (E³ 2.0) ，将包含有竞争力的统一操作系统，并为自动驾驶Level4做好准备
        2.  E3 1.2 是 PPE\PPC，奥迪和保时捷的新平台，专注整车的网络拓扑和功能，和物理结构没有必然联系
        3.  搜整车网络架构
            1.  EEA: Electrical/Electronic Architecture。
        4.  有些架构是有数据备份的，不仅仅有一个链接，可能有多个信息的链接
        5.  测试车基本都是有测试线束的，会把各个总线引出来，再把logger的信息记录下来。可以录制部分的内容或者全部的内容；不同总线之间的信息交互是通过网关做路由(route)的。又比如以太网的信号，路由了再发送到can总线上

![picture 3](images/d595d2a978d5850b9dbc5bd33b5a370170151b286c420d4ae5329fc3a3a23319.png)  


1. 关于Can
   1. 使用双绞线来传输信号，是世界上应用最广泛的现场总线之一。
   2. CAN总线是一种串行数据通信总线，其通信速率最高可达1 Mb/s。CAN系统内两个任意节点之间的最大传输距离与其位速率有关。
   3. CAN之前的汽车ECU是复杂的点对点布线
   4. 两线式总线结构，电气信号为差分式；
   5. 多主控制，在总线空闲时，所有的单元都可开始发送消息，最先访问总线的单元可获得发送权；多个单元同时开始发送时，发送高优先级ID消息的单元可获得发送权；
   6. 点对点控制，一点对多点及全局广播几种传送方式接收数据，网络上的节点可分成不同的优先级，可以满足不同的实时要求；
   7. 采用非破坏性位仲裁总线结构机制，当两个节点同时向网络上传送信息时，优先级低的节点主动停止数据发送，而优先级高的节点可不受影响地继续传送数据
   8. 消息报文不包含源地址或者目标地址，仅通过标识符表明消息功能和优先级；
   9. 基于固定消息格式的广播式总线系统，短帧结构；
   10. 事件触发型，只有当有消息要发送时，节点才向总线上广播消息；
   11. 可以通过发送远程帧请求其它节点发送数据；
   12. 消息数据长度0~8Byte；
   13. 节点数最多可达110个；
   14. 错误检测功能。所有节点均可检测错误，检测处错误的单元会立即通知其它所有单元；
   15. 发送消息出错后，节点会自动重发；
   16. 故障限制，具有自动关闭总线的功能，节点控制器可以判断错误是暂时的数据错误还是持续性错误，当总线上发生持续数据错误时，控制器可将节点从总线上隔离，以使总线上的其他操作不受影响；
   17. 理论上，CAN总线用单根信号线就可以通信，但还是配备了第二根导线，第二根导线与第一根导线信号为差分关系，可以有效抑制电磁干扰；
   18. 总线上可同时连接多个节点，可连接节点总数理论上是没有限制的，但实际可连接节点数受总线上时间延迟及电气负载的限制。
   19. 每帧信息都有CRC校验及其他检错措施，数据错误率极低；

![picture 0](images/9bb3617efb0690e345a283de37cb05a3696f61bab8869757576b1c477c10a9c9.png)  

![picture 1](images/7a7d9e5f48616eb4211e714e80b4c500f019590aac404c1880b4b92b2b583b8a.png)  

![picture 2](images/433e1cf1404f4b9eda83a47c2e8ce71731fe69667bb8797e944fe6eb97c840f9.png)  


2. 关于LIN
   1. 局部互联协议LIN
   2. (Local Interconnect Network)是面向汽车地段分布式应用的低成本的串行通讯网络，用于实现汽车中的分布式电子系统控制。LIN 的目标是为现有汽车网络(例如CAN 总线)提供辅助功能，因此LIN总线是一种辅助的总线网络。在不需要CAN 总线的带宽和多功能的场合，比如智能传感器和制动装置之间的通讯使用LIN 总线可大大节省成本。
   3. 仅使用一根12V 信号总线和一个无固定时间基准的节点同步时钟线。

3. 关于Flexray
   1. 高速容错网络协议FlexRay
   2. FlexRay总线是由宝马、飞利浦、飞思卡尔和博世等公司共同制定的一种新型通信标准， 专为车内联网而设计， 采用基于时间触发机制， 具有高带宽、容错性能好等特点， 在实时性、可靠性和灵活性方面具有一定的优势。
   3. 利用时间触发通信时， 网络中的各个节点都预先知道彼此将要进行通信的时间， 接收器提前知道报文到达的时间， 报文在总线上的时间可以预测出来。
   4. 它采用了周期通信的方式， 一个通信周期可以划分为静态部分、动态部分、特征窗和网络空闲时间4个部分。静态部分和动态部分用来传输总线数据，即FlexRay报文。特征窗用来发送唤醒特征符和媒介访问检测特征符。网络空闲时间用来实现分布式的时钟同步和节点参数的初始化。FlexRay具有高速、可靠及安全的特点。
4. 各种传感器
   1. Lidar：上位机软件用于显示实时点云图及回放功能，采集用Wireshark。

![picture 4](images/f60bcd009326a359bfb74e667f2fa45c88b55881a2f0a02bb3dbdf4d6e409a49.png)  
