import sys
import os
import psutil
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox,
                               QHeaderView, QComboBox)
from PySide6.QtCore import QTimer, QDateTime, Qt
from PySide6.QtGui import QIcon

class ProcessKillerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_processes = []
        self.current_lang = "zh"  # 默认中文，可改为"en"切换英文
        self.lang_res = {  # 语言资源字典
            "en": {
                "window_title": "PythonProcessKiller-PythonVersion",
                "search_placeholder": "Search script path keywords...",
                "table_headers": ["PID", "Script Path", "Runtime", "Status", "Action"],
                "refresh_btn": "Manual Refresh",
                "kill_btn": "Terminate",
                "unknown_script": "Unknown script",
                "success_title": "Success",
                "success_msg": "Attempted to terminate process PID: ",
                "error_no_proc_title": "Error",
                "error_no_proc_msg": "Process PID: no longer exists",
                "error_access_title": "Error",
                "error_access_msg": "No permission to terminate process PID: (Please try running as administrator)"
            },
            "zh": {
                "window_title": "Python进程杀手-Python版",
                "search_placeholder": "搜索脚本路径关键词...",
                "table_headers": ["PID", "脚本路径", "运行时长", "状态", "操作"],
                "refresh_btn": "手动刷新",
                "kill_btn": "关闭",
                "unknown_script": "未知脚本",
                "success_title": "成功",
                "success_msg": "已尝试终止进程 PID: ",
                "error_no_proc_title": "错误",
                "error_no_proc_msg": "进程 PID: 已不存在",
                "error_access_title": "错误",
                "error_access_msg": "无权限终止进程 PID: （请尝试以管理员身份运行）"
            }
        }
        self.init_ui()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_processes)
        self.timer.start(2000)
        self.refresh_processes()
        self.set_window_icon()

    def set_window_icon(self):
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)
        icon_path = resource_path("favicon.ico")
        self.setWindowIcon(QIcon(icon_path))

    def init_ui(self):
        self.setWindowTitle(self.lang_res[self.current_lang]["window_title"])
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 语言切换下拉框
        self.lang_switch = QComboBox()
        self.lang_switch.addItems(["English", "中文"])
        self.lang_switch.setCurrentIndex(0 if self.current_lang == "en" else 1)
        self.lang_switch.currentIndexChanged.connect(self.switch_language)
        layout.addWidget(self.lang_switch)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(self.lang_res[self.current_lang]["search_placeholder"])
        self.search_input.textChanged.connect(self.filter_processes)
        layout.addWidget(self.search_input)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(self.lang_res[self.current_lang]["table_headers"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.Interactive)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.Interactive)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        layout.addWidget(self.table)

        self.refresh_btn = QPushButton(self.lang_res[self.current_lang]["refresh_btn"])
        self.refresh_btn.clicked.connect(self.refresh_processes)
        layout.addWidget(self.refresh_btn)

    def switch_language(self, index):
        # 切换语言并刷新界面
        self.current_lang = "en" if index == 0 else "zh"
        self.update_ui_text()
        self.refresh_processes()  # 刷新表格内容（含按钮文本）

    def update_ui_text(self):
        # 更新静态UI文本
        self.setWindowTitle(self.lang_res[self.current_lang]["window_title"])
        self.search_input.setPlaceholderText(self.lang_res[self.current_lang]["search_placeholder"])
        self.table.setHorizontalHeaderLabels(self.lang_res[self.current_lang]["table_headers"])
        self.refresh_btn.setText(self.lang_res[self.current_lang]["refresh_btn"])

    def get_python_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'exe', 'create_time']):
            try:
                if proc.info['name'] in ('python.exe', 'pythonw.exe'):
                    cmdline = proc.cmdline()
                    # 使用语言资源中的"未知脚本"文本
                    script_path = cmdline[1] if len(cmdline) > 1 else self.lang_res[self.current_lang]["unknown_script"]
                    
                    create_time = QDateTime.fromMSecsSinceEpoch(int(proc.info['create_time'] * 1000))
                    duration = create_time.secsTo(QDateTime.currentDateTime())
                    hours, remainder = divmod(duration, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    duration_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                    
                    processes.append({
                        'pid': proc.info['pid'],
                        'script_path': script_path,
                        'duration': duration_str,
                        'status': proc.status()
                    })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return processes

    def refresh_processes(self):
        self.table.setRowCount(0)
        self.current_processes = self.get_python_processes()
        self.filter_processes()

    def filter_processes(self):
        keyword = self.search_input.text().lower()
        filtered = [p for p in self.current_processes if keyword in p['script_path'].lower()]
        
        self.table.setRowCount(len(filtered))
        for row, proc in enumerate(filtered):
            self.table.setItem(row, 0, QTableWidgetItem(str(proc['pid'])))
            
            path_item = QTableWidgetItem(proc['script_path'])
            path_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            path_item.setToolTip(proc['script_path'])
            self.table.setItem(row, 1, path_item)
            
            self.table.setItem(row, 2, QTableWidgetItem(proc['duration']))
            self.table.setItem(row, 3, QTableWidgetItem(proc['status']))
            
            # 使用当前语言的"关闭"/"Terminate"文本
            kill_btn = QPushButton(self.lang_res[self.current_lang]["kill_btn"])
            kill_btn.clicked.connect(lambda _, pid=proc['pid']: self.kill_process(pid))
            self.table.setCellWidget(row, 4, kill_btn)
        
        self.table.resizeColumnsToContents()

    def kill_process(self, pid):
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            # 使用当前语言的成功提示
            QMessageBox.information(
                self, 
                self.lang_res[self.current_lang]["success_title"], 
                f"{self.lang_res[self.current_lang]['success_msg']}{pid}"
            )
            self.refresh_processes()
        except psutil.NoSuchProcess:
            QMessageBox.warning(
                self, 
                self.lang_res[self.current_lang]["error_no_proc_title"], 
                f"{self.lang_res[self.current_lang]['error_no_proc_msg']}{pid}"
            )
        except psutil.AccessDenied:
            QMessageBox.warning(
                self, 
                self.lang_res[self.current_lang]["error_access_title"], 
                f"{self.lang_res[self.current_lang]['error_access_msg']}{pid}"
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProcessKillerApp()
    window.show()
    sys.exit(app.exec_())