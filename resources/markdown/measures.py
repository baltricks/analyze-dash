from dash import dcc

measures = { 'en' : 
    dcc.Markdown('''
        Let $n$ be the number of values in a data set $\\{x_1, x_2, ... x_n\\}$.

        The **mean** value is the *arithmetic mean* of a data set.

        $$
        \\bar{x} = \\bar{x}_{arithm} = \\frac{1}{n}\\displaystyle\\sum_{i=0}^{n}{x_i} \\tag{1.1}
        $$

        The **median** value is another kind of mean value. In the ordered list 
        of the values it's the *central value*:

        $$
        \\bar{x}_{median} =
        \\begin{cases}
            x_{[\\frac{n+1}{2}]}  & \\quad \\text{if } n \\text{ is odd}\\\\
            \\frac{1}{2} (x_{[\\frac{n}{2}]} + x_{[\\frac{n}{2} + 1]}) & \\quad \\text{if } n \\text{ is even}
        \\end{cases}
        \\tag{1.2}
        $$
    ''', mathjax=True)
}