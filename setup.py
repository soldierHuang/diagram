# # setup.py

# setup.py

import os
from setuptools import find_packages, setup

# 讀取 README.md 作為 long_description
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A test project."


setup(
    name="diagram",  # Required: 套件的名稱
    version="0.0.1",  # Required: 版本號
    author="linsam",  # Optional: 作者
    author_email="samlin266118@gmail.com",  # Optional: 作者信箱
    description="test",  # Optional: 簡短描述
    long_description=long_description,  # Optional: 詳細描述 (來自 README.md)
    long_description_content_type="text/markdown",  # Optional: 告訴 PyPI 這是 Markdown 格式

    # --- 關鍵修改在這裡 ---
    # 自動尋找專案中的所有 Python 套件 (即包含 __init__.py 的目錄)
    packages=find_packages(),
    # ----------------------

    # 如果你的程式碼在 src/ 目錄下，請使用以下兩行取代上面的 `packages`
    # package_dir={"": "src"},
    # packages=find_packages(where="src"),

    classifiers=[  # Optional: 套件的分類標籤，幫助使用者搜尋
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # 建議加上授權條款
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8', # 建議明確指定支援的 Python 版本
)


# import os
# from io import open

# from setuptools import find_packages, setup

# here = os.path.abspath(os.path.dirname(__file__))
# with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
#     long_description = f.read()
#     print(long_description)


# setup(
#     name="diagram",  # Required
#     version="0.0.1",  # Required
#     description="test",  # Optional
#     long_description=long_description,  # Optional
#     long_description_content_type="text/markdown",  # Optional (see note above)
#     author="linsam",  # Optional
#     author_email="samlin266118@gmail.com",  # Optional
#     classifiers=[  # Optional
#         "Development Status :: 3 - Alpha",
#     ],
#     # packages=find_packages(where="src"),
#     # package_dir={"": "src"},
# )
