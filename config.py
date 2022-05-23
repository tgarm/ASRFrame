import platform
import os

from dotenv import load_dotenv

load_dotenv()

project_path = os.path.split(os.path.realpath(__file__))[0] #

thu_datapath = None # 目录下应该有data/ dev/ 等目录
z200_datapath = None # 目录下应该有一大堆G../格式的目录
aishell_datapath = None # 目录下应有wav/和transcript/两个目录
prime_datapath = None # 目录下应有一个json文件和一个目录
stcmd_datapath = None # 目录下应该直接是音频文件

wiki_datapath = None

if platform.system() == "Linux":
    thu_datapath = os.getenv("THU_DATAPATH")
    z200_datapath = os.getenv("Z200_DATAPATH")
    aishell_datapath = os.getenv("AISHELL_DATAPATH")
    prime_datapath = os.getenv("PRIME_DATAPATH")
    stcmd_datapath = os.getenv("STCMD_DATAPATH")
    wiki_datapath = os.getenv("WIKI_DATAPATH")
elif platform.system() == "Windows":
    thu_datapath = r"C:\E\jupyter_notebook\voice_reco\Dataset\thchs30"
    z200_datapath = r"C:\E\jupyter_notebook\voice_reco\Dataset\z200"
    aishell_datapath = r"C:\E\jupyter_notebook\voice_reco\Dataset\data_aishell"
    prime_datapath = r"C:\E\jupyter_notebook\voice_reco\Dataset\primewords_md_2018_set1"
    stcmd_datapath = r"C:\E\jupyter_notebook\voice_reco\Dataset\ST-CMDS-20170001_1-OS"

model_dir = os.path.join(project_path,"model") # ./model
dict_dir = os.path.join(project_path,"util","dicts") #./util/dicts

acoustic_model_dir = os.path.join(model_dir, "acoustic") # ./acoustic
language_model_dir = os.path.join(model_dir, "language") # ./language

loss_dir = "./loss_plot/"
acoustic_loss_dir = os.path.join(loss_dir,"acoustic") # ./loss_plot/acoustic
language_loss_dir = os.path.join(loss_dir,"language") # ./loss_plot/language

join_model_path = lambda x:os.path.join(model_dir, x)

chs_dict_path = os.path.join(dict_dir,"pure_chs.txt") # ./util/dicts/...
py_dict_path = os.path.join(dict_dir,"pure_py.txt") # ./util/dicts/...
err_dict_path = os.path.join(dict_dir,"err_dict.json")
