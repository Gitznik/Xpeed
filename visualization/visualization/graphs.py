import altair as alt


def line_chart(df):
    return alt.Chart(df).mark_line().encode(x="date", y="val").interactive()
