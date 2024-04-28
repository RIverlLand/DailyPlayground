量产车：
国外代表的 特斯拉 FFD 12.0.3 纯视觉，端到端（传统智驾是：感知（视觉，点云，毫米波，4D毫米波雷达）-，新颖，
L2 ++
纯OA？

Adas：L0-L2，可能到不了L3 L4。

1. Create, manage and steer testing and validation processes for the L2 driver assistance development projects.
   - L2:驾驶操作是车辆，但是人要监管；巡航、跟车、APA泊车、城市NOA之类的；
   - 根据项目进行测试：比如AEB,ACC,LKA各个，独立进行功能测试；可以是function导向的也可以是场景导向的
   - 大概流程：整车的EE开发中，有个klausur team：周期性的软件更新、比如三个月一个大版本，每段时间一个sprint，每个sprint就会有一个窗口期，交付软件；由klausur的人刷软件到车上去测试，反馈问题，在接下来的sprint里做修复；最终的release中定下来一个表现好的sprint的状态，作为整车版本的release。**大众的体系里叫做VR，Verbund release**
     - 每个VR release之后会进行长周期的测试，比如冬测或者夏测；是不是最终进入SOP的才会测试还是很多都会测试就不清楚。
     - 比如大众sprint是两周，一个VR是三个sprint，所以基本VR是1.5个月，但不是每个VR都会做工业化，可能三个VR才做一个工业化，让供应商来做最终的更改。
     - 比如一个新车型实装，定在五月，不会去改sprint的时间，而是根据装车节点去选取哪个sprint作为装车的状态。
1. Design test scenario and test cases, maintain the test cases accroding to the requirements changes.
2. Collaborate with the component, system and function developers of for requirement break-down.
   1. component: 主管是比如奔驰的BTV；component是负责硬件区的，比如谁负责相机。。。比如空调：谁管压缩机，出风口；又比如body controller的硬件是简单的，system的owner就很复杂，E\E system owner（电子电气）或者speaker才能解决一些细节的问题，比如为什么尾灯不亮了
   2. system: 是系统？基本是搞软件的，对于功能的控制逻辑比较清楚。比如谁负责空调的软件，涉及到很多sensor，阀门，
      1. 行车域和泊车域（域控制就是功能区分的，比如智驾域、泊车域）
      2. 域控制器（和架构相关）：分布式、耦合式还是什么
         1. 座舱域是用来车机的控制，
         2. 智驾域是包含车外摄像头、雷达、域控制器等部分集成，和座舱通讯等等；查查GMSL接口？Can信号？
         3. 车身、地盘、信息娱乐、adas域、链接域，基本是通过功能区分的
   3. function: 第一点中的？
3. Ensure the tracibility between the requirements and test catalogue.
   1. 测试的问题需要能够重现
4. Use testing equipement (Vector, ODIS,..) to Reproduce the customer compliants and record traces.
   1. Vector：是个德国品牌，软件是CanOE，用来做Can总线上的全套工具链？总线的仿真，信号的截取分析编程blablabla（CAN总线上，信号表现为电压形式，通过CAN_H和CAN_L线上的电位差来表示CAN信号）；录一录trace，总线的报文；
      1. 报文：can总线的数据是有很多位，起始、仲裁、数据、校验、帧结束之类的，组成了一个PDU；但是由于电瓶位不稳定，会有很多校验位
      2. can,lan,以太网,flexray
   2. ODIS：大众自己的诊断工具（通过OBD去车子的诊断界面,OBD是主控下的一个接口？）
5. Ability to conduct pre-analysis to locate the root-cause.
6. Track the bug-fix process, coordinate the JVs and Supplier to ensure quick and effective bug-fixing
   1. JVs：合资公司
7. Fleet-management, partially support on testing fleet management and test route plan
   1. 管车，一般上车跑的是三方测试公司
   2. 协调车的改造，提需求，下工单，管车的状态，测试目标
   3. function list 在大众叫Fuli = function list
8.  Knowledge in OEM development process and overall vehicle architecture
    1.  白车身的造型、blablabla，和我们没关系
    2.  每个车都是在一个平台上开发的，比如后驱，四驱，前驱，这样不同的设计可以沿用电气、设计等等
    3.  还会有扩展车，延申车型，比如领克01 05，就是同一车型的不同style
        1.  E3 2.0 是 SSP平台
        2.  E3 1.2 是 PPE\PPC，奥迪和保时捷的新平台，专注整车的网络拓扑和功能，和物理结构没有必然联系
        3.  搜整车网络架构
        4.  有些架构是有数据备份的，不仅仅有一个链接，可能有多个信息的链接
        5.  测试车基本都是有测试线束的，会把各个总线引出来，再把logger的信息记录下来。可以录制部分的内容或者全部的内容；不同总线之间的信息交互是通过网关做路由的。又比如以太网的信号，路由了再发送到can总线上
9.  