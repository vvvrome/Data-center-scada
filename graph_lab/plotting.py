import matplotlib.pyplot as plt


def preparar_grafica(
    figsize=(10, 6),
    titulo=None,
    xlabel=None,
    ylabel=None
):

    fig, ax = plt.subplots(
        figsize=figsize,
        facecolor="#111827"
    )

    ax.set_facecolor("#0f172a")

    if titulo:
        ax.set_title(
            titulo,
            color="#f8fafc",
            fontsize=16,
            fontweight="bold",
            pad=15
        )

    if xlabel:
        ax.set_xlabel(
            xlabel,
            color="#cbd5e1",
            fontsize=11
        )

    if ylabel:
        ax.set_ylabel(
            ylabel,
            color="#cbd5e1",
            fontsize=11
        )

    ax.tick_params(
        colors="#94a3b8",
        labelsize=10
    )

    for spine in ax.spines.values():
        spine.set_color("#334155")

    ax.grid(
        True,
        color="#475569",
        alpha=0.20,
        linestyle="--",
        linewidth=0.8
    )

    return fig, ax