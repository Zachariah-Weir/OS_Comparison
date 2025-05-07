from comparisons import *


title = 'Fault Isolation Recovery Time Comparison'
ylabel = 'Recovery Time (seconds)'
xlabel = 'Kernel Architecture'
values = [.038833, .004359]
xlabels = ['Monolithic', 'Microkernel']
plot_bar_graph( title, ylabel, xlabel, values, xlabels )


title = 'System Call Performance Comparison'
ylabel = 'System Call Time (seconds)'
xlabel = 'Kernel Architecture'
values = [.0068, .0248]
xlabels = ['Monolithic', 'Microkernel']
plot_bar_graph( title, ylabel, xlabel, values, xlabels )


title = 'Boot Time Comparison'
ylabel = 'Boot Time (seconds)'
xlabel = 'Kernel Architecture'
values = [.0350, .0363]
xlabels = ['Monolithic', 'Microkernel']
plot_bar_graph( title, ylabel, xlabel, values, xlabels )