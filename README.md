# English:
# PythonProcessKiller-Py - Python Process Management Tool

![GitHub release (latest by date)](https://img.shields.io/github/v/release/add-qwq/PythonProcessKiller-Py?style=flat-square)  
![GitHub stars](https://img.shields.io/github/stars/add-qwq/PythonProcessKiller-Py?style=flat-square)  
![Python version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)  
![License](https://img.shields.io/github/license/add-qwq/PythonProcessKiller-Py?style=flat-square)  

This is the **Python version** of the Python process management tool, with a corresponding **[C# version](https://github.com/add-qwq/PythonProcessKiller-Csharp)** available (suitable for scenarios requiring high-speed operation and long-term maintenance). The Python version focuses on **rapid development and flexible modification**, supporting direct invocation in development environments. Precompiled EXEs are also provided (suitable for temporary use, though slightly Slower than the C# version). Easily manage Python processes through a visual interface to solve the tedious process of manually searching and terminating them in Task Manager.


## 🌟 Key Features  
- **Real-Time Monitoring**: Automatically refreshes every 2 seconds to display all current Python processes (`python.exe`/`pythonw.exe`), showing PID, script path, runtime, and status.  
- **Multi-Language Support**: Switch between **Simplified Chinese/English** with one click (via the top-right dropdown menu), no additional language packs required.  
- **Process Filtering**: Use the search box to input keywords from script paths for quick filtering (supports fuzzy matching).  
- **Safe Termination**: Click the "Terminate" button to attempt stopping specified processes, with automatic handling of exceptions like lack of permissions or already exited processes (with clear prompts).  
- **Information Visualization**: Script paths support hover tooltips (friendly for long paths), runtime is formatted as `HH:MM:SS`, and status syncs with system process status in real time.  


## 🚀 Quick Start  

### Option 1: Download Prebuilt EXE (Recommended for Temporary Use)  
No Python or dependencies needed:  
1. Go to the [Releases page](https://github.com/add-qwq/PythonProcessKiller-Py/releases).  
2. Download `PythonProcessKiller-Py-EXE.zip` and extract it.  
3. You’ll find two executables: `PythonProcessKiller-EN.exe` (English) and `PythonProcessKiller-CN.exe` (Chinese). Double-click to run.  


### Option 2: Run from Source Code (For Development/Modification)  
Requires a Python environment, ideal for debugging and customization:  

#### Prerequisites  
- Python 3.8+  
- Install dependencies (one command):  
  ```bash  
  pip install pyside6 psutil  
  ```  

#### Steps  
1. Download source code:  
   - Click `Code → Download ZIP` on the [GitHub repo](https://github.com/add-qwq/PythonProcessKiller-Py) (no Git needed).  
   - Extract the ZIP to your preferred location.  

2. Run the program:  
   ```bash  
   cd PythonProcessKiller-Py  # Navigate to project root  
   python PythonProcessKiller.py  # Launch (default language: Chinese, switchable in UI)  
   ```  


## 📦 Package into EXE (Custom Build)  
Use `pyinstaller` to create standalone EXEs (install first: `pip install pyinstaller`).  

### Example Command (Windows):  
```bash  
# Go to project root  
cd PythonProcessKiller-Py  

# Packaging command  (ensure favicon.ico exists)  
pyinstaller -w -F -i favicon.ico --add-data "favicon.ico;." PythonProcessKiller.py  

# Parameters:  
# -w: Hide console window (GUI apps).  
# -F: Generate single EXE file.  
# -i: Set window icon (favicon.ico in project root).  
# --add-data: Include icon assets (use ":" instead of ";" on macOS/Linux).  
```  


## 🖥 Interface Overview  
![English Interface](https://github.com/add-qwq/PythonProcessKiller-Py/raw/main/PythonProcessKiller-Py-EN.png?raw=true)  
*Switch languages via the Top dropdown menu. All features are identical across languages.*  


## 📘 Usage Examples  

### Example 1: Quick Terminate a Specific Python Process  
**Goal**: Terminate a Python process with a script path containing `test_script.py`.  

**Steps**:  
1. After launching, the interface auto-loads all current Python processes (refreshes every 2s).  
2. Enter `test_script.py` in the search box to filter target processes (matching keywords in the Script Path column are highlighted).  
3. Find the target process row and click the "Terminate" button.  
4. On success, a prompt appears: `Attempted to terminate process PID: 1234`. If the process has exited or lacks permissions, a specific error message shows (e.g., "Process PID: 1234 no longer exists" or "No permission to terminate PID: 1234 (run as admin)").  


### Example 2: Monitor Long-Running Python Processes  
**Goal**: Check how long a Python script has been running.  

**Steps**:  
1. Launch the app and locate the target process (filter by path keywords if needed).  
2. Check the "Runtime" column (formatted as `HH:MM:SS`), e.g., `01:23:45` means 1 hour 23 minutes 45 seconds.  
3. The program auto-refreshes data every 2s, updating the runtime in real time.  


### Example 3: Handle Permission Issues When Terminating Processes  
**Goal**: Resolve "no permission to terminate" errors.  

**Steps**:  
1. If a prompt appears: "No permission to terminate process PID: 1234 (Please try running as administrator)".  
2. Right-click the EXE or Python script and select "Run as Administrator".  
3. Retry terminating the process with elevated permissions.  


## 📜 License  
This project is licensed under the [Apache License 2.0](https://github.com/add-qwq/PythonProcessKiller-Py/blob/main/LICENSE).  


## 🙋 Contributing & Feedback  
- **Bug Reports/Feature Requests**: Submit an [Issue](https://github.com/add-qwq/PythonProcessKiller-Py/issues).  
- **Code Contributions**: Fork the repo, make changes, and submit a PR (welcome to optimize the UI or add filtering rules).  
- **Localization**: To add new languages, update the `lang_res` dictionary in the code (reference `zh` and `en` configurations).  


---  

# 中文：
# PythonProcessKiller-Py - Python 进程管理工具  

![GitHub release (latest by date)](https://img.shields.io/github/v/release/add-qwq/PythonProcessKiller-Py?style=flat-square)  
![GitHub stars](https://img.shields.io/github/stars/add-qwq/PythonProcessKiller-Py?style=flat-square)  
![Python version](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square)  
![License](https://img.shields.io/github/license/add-qwq/PythonProcessKiller-Py?style=flat-square)  

本项目为 **Python 进程管理工具** 的 Python 版本实现，配套存在 **[C# 版本](https://github.com/add-qwq/PythonProcessKiller-Csharp)**（适合需要高速运行、长期维护的场景）。Python 版侧重 **快速开发与灵活修改**，支持直接在开发环境中调用运行，也提供预编译 EXE（适合临时使用，但运行速度略慢于 C# 版）。通过可视化界面轻松管理 Python 进程，解决手动去任务管理器先查找再终止的繁琐过程  


## 🌟 核心功能  
- **实时监控**：自动刷新（每2秒）并展示当前所有 Python 进程（含 `python.exe`/`pythonw.exe`），显示 PID、脚本路径、运行时长及状态。  
- **多语言支持**：界面支持 **简体中文/英文** 一键切换（右上角下拉菜单），无额外语言包依赖。  
- **进程筛选**：通过搜索框输入脚本路径关键词，快速过滤目标进程（支持模糊匹配）。  
- **安全终止**：点击「关闭」按钮可尝试终止指定进程，自动处理无权限/进程已退出等异常场景（含明确提示）。  
- **信息可视化**：脚本路径支持悬停提示（长路径友好），运行时长格式化为 `HH:MM:SS`，状态实时同步系统进程状态。  


## 🚀 快速开始  

### 方式 1：下载预编译 EXE（推荐临时使用）  
无需安装 Python 或依赖：  
1. 前往 [Releases 页面](https://github.com/add-qwq/PythonProcessKiller-Py/releases)。  
2. 下载 `PythonProcessKiller-Py-EXE.zip` 并解压。  
3. 解压后包含两个可执行文件：`PythonProcessKiller-EN.exe`（英文）和 `PythonProcessKiller-CN.exe`（中文），双击运行即可。  


### 方式 2：从源代码运行（适合开发/修改）  
需 Python 环境，支持快速调试与二次开发：  

#### 环境要求  
- Python 3.8+  
- 安装依赖（仅需一步）：  
  ```bash  
  pip install pyside6 psutil  
  ```  

#### 步骤  
1. 下载源代码：  
   - 在 [GitHub 仓库](https://github.com/add-qwq/PythonProcessKiller-Py) 点击 `Code → 下载 ZIP`（无需 Git）。  
   - 解压 ZIP 文件至目标位置。  

2. 运行程序：  
   ```bash  
   cd PythonProcessKiller-Py  # 进入项目根目录  
   python PythonProcessKiller.py  # 启动程序（默认语言为中文，可通过界面切换）  
   ```  


## 📦 打包为 EXE（自定义发布）  
使用 `pyinstaller` 生成独立 EXE（需先安装：`pip install pyinstaller`）。  

### 打包命令示例（Windows）：  
```bash  
# 进入项目根目录  
cd PythonProcessKiller-Py  

# 打包命令（需确保 favicon.ico 存在）  
pyinstaller -w -F -i favicon.ico --add-data "favicon.ico;." PythonProcessKiller.py  

# 参数说明：  
# -w：隐藏控制台窗口（图形界面程序推荐）。  
# -F：生成单个 EXE 文件（非目录）。  
# -i：指定窗口图标（项目根目录的 favicon.ico）。  
# --add-data：包含图标资源（Windows 用 `;`，macOS/Linux 用 `:`）。  
```  


## 🖥 界面概览  
![中文界面](https://github.com/add-qwq/PythonProcessKiller-Py/raw/main/PythonProcessKiller-Py-CN.png?raw=true)  
*(通过顶部下拉菜单切换中英文，功能完全一致。)*  


## 📘 使用示例  

### 示例 1：快速终止指定 Python 进程  
**目标**：终止运行路径包含 `test_script.py` 的 Python 进程。  

**步骤**：  
1. 启动程序后，界面自动加载当前所有 Python 进程（默认每2秒刷新）。  
2. 在搜索框输入 `test_script.py`，过滤出目标进程（脚本路径列会高亮匹配关键词）。  
3. 找到对应进程行，点击「关闭」（中文）或「Terminate」（英文）按钮。  
4. 若成功，弹出提示：`已尝试终止进程 PID: 1234`（中文）；若进程已退出或无权限，会提示具体原因（如「进程 PID: 1234 已不存在」或「无权限终止进程 PID: 1234（请尝试以管理员身份运行）」）。  


### 示例 2：监控长时间运行的 Python 进程  
**目标**：查看某个 Python 脚本已运行的时长。  

**步骤**：  
1. 启动程序，在表格中找到目标进程（可通过搜索框过滤路径关键词）。  
2. 查看「运行时长」列（格式为 `HH:MM:SS`），例如 `01:23:45` 表示已运行1小时23分45秒。  
3. 程序自动每2秒刷新数据，运行时长会实时更新。  


### 示例 3：处理无权限终止进程的场景  
**目标**：解决「无权限终止进程」的问题。  

**步骤**：  
1. 尝试终止进程时，若弹出提示「无权限终止进程 PID: 1234（请尝试以管理员身份运行）」（中文）。  
2. 右键点击 EXE 或 Python 脚本，选择「以管理员身份运行」。  
3. 重新尝试终止进程，权限问题解决后即可操作。  


## 📜 许可证  
本项目采用 [Apache 2.0 许可证](https://github.com/add-qwq/PythonProcessKiller-Py/blob/main/LICENSE)。  


## 🙋 贡献与反馈  
- **问题反馈/功能建议**：提交 [Issue](https://github.com/add-qwq/PythonProcessKiller-Py/issues)。  
- **代码贡献**：Fork 仓库，修改后提交 PR（欢迎优化界面、增加进程筛选规则等）。  
- **多语言支持**：如需添加其他语言，可在 `lang_res` 字典中补充翻译（参考代码中的 `zh` 和 `en` 配置）。  
