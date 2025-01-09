import os
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 配置 Matplotlib 使用中文字体（SimHei）
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False


def process_png_to_rgb(input_path, output_path, preview=True, target_size=(1024, 1024)):
    """
    处理 PNG 图像，将其转换为 RGB 三通道，调整为指定大小，并保存到指定路径。

    参数:
    - input_path (str): 输入图像路径。
    - output_path (str): 处理后保存的图像路径。
    - preview (bool): 是否预览处理后的图像 (默认: True)。
    - target_size (tuple): 调整图像的目标大小 (默认: 1024x1024)。
    """
    # 检查输入路径是否存在
    if not os.path.exists(input_path):
        print(f"输入路径不存在: {input_path}")
        return

    # 打开图像
    image = Image.open(input_path)

    # 检查是否为 4 通道 (RGBA)
    if image.mode == 'RGBA':
        print("检测到 4 通道 (RGBA) 图像，正在转换为 RGB...")
        image = image.convert('RGB')  # 转换为 RGB
    elif image.mode != 'RGB':
        print(f"检测到非 RGB 模式图像 ({image.mode})，正在转换为 RGB...")
        image = image.convert('RGB')
    else:
        print("图像已是 RGB 模式，无需转换。")

    # 调整图像大小
    print(f"正在调整图像大小到: {target_size}")
    image = image.resize(target_size, Image.Resampling.LANCZOS)  # 使用 LANCZOS 作为高质量的重采样方法

    # 保存处理后的图像
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # 确保输出目录存在
    image.save(output_path)
    print(f"处理后的图像已保存到: {output_path}")

    # # 预览处理后的图像
    # if preview:
    #     plt.imshow(image)
    #     plt.axis('off')
    #     plt.title("预览处理后的图像")
    #     plt.show()


# 示例用法
if __name__ == "__main__":
    input_image_path = "/home/iris/Datasets/mua/test/T1/0001.png"  # 输入图像路径
    output_image_path = "/home/iris/Datasets/mua/test/T1/0003.png"  # 输出图像路径
    process_png_to_rgb(input_image_path, output_image_path)
