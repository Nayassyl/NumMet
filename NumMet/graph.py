root1 = fixed_point_method(0)
root2 = fixed_point_method(1)
plt.scatter([root1, root2], [equation(root1),
    equation(root2)], color="red", marker="o")
plt.annotate(f'Root 1: ({root1:.10f}, {equation(root1):.10f})', xy=(root1, equation(root1)), xytext=(
    root1-10, equation(root1)-10), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")
plt.annotate(f'Root 2: ({root2:.10f}, {equation(root2):.10f})', xy=(root2, equation(root2)), xytext=(
    root2+1, equation(root2)+1), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")

plt.annotate(f'Root 1: ({root1:.10f}, {equation(root1):.10f})', xy=(root1, equation(root1)), xytext=(
    root1-10, equation(root1)-10), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")
plt.annotate(f'Root 2: ({root2:.10f}, {equation(root2):.10f})', xy=(root2, equation(root2)), xytext=(
    root2+1, equation(root2)+1), arrowprops=dict(arrowstyle='->'), fontsize=10, color="red")