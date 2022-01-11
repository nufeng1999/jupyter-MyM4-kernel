from ipykernel.kernelapp import IPKernelApp
from .kernel import M4Kernel
IPKernelApp.launch_instance(kernel_class=M4Kernel)
