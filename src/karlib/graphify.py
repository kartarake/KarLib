def valuediff(ypos,i):
    if i>len(ypos)-2:
        return 0
    return ypos[i] - ypos[i+1]

def graphify(values:list|tuple) -> str:
    """Creates a string representing a graph of the given plots. Only supports continues plots.
    Plot value example: [(x1,y1), (x2,y2), (x3,y3), ...]

    Args:
        values (list | tuple): The values of plots in a list.

    Raises:
        ValueError: If the graph range is zero.

    Returns:
        str: The string representing the graph
    """    
    if values is None or len(values) == 0:
        raise ValueError("values must not be null or empty")

    xvalues = []
    yvalues = []
    for tuple in values:
        xvalues.append(tuple[0])
        yvalues.append(tuple[1])

    valuerange = max(xvalues) - min(xvalues)
    margin = valuerange / 10    
    upperlimit = max(yvalues) + margin
    lowerlimit = min(yvalues) - margin

    graphrange = upperlimit - lowerlimit
    if graphrange == 0:
        raise ValueError("graphrange must not be zero")

    graphunit = graphrange / 10
    graphmarked = []
    for i in range(1,11):
        graphmarked.append(graphunit*i)
    
    ypos = []
    for i in yvalues:
        for j in range(len(graphmarked)):
            if i < graphmarked[j]:
                ypos.append(len(graphmarked) - 1 - j)
                break
    
    graph = []
    for i in range(10):
        graph.append([])
    
    for i in range(len(ypos)):
        column = list(" " * 10)
        diff = valuediff(ypos,i)
        if diff == 0:
            column[ypos[i]] = "_"
        elif diff == 1:
            column[ypos[i]] = "/"
        elif diff == -1:
            column[ypos[i]] = "\\"
        elif diff > 1:
            for j in range(diff):
                column[ypos[i]-j] = "|"
                column[ypos[i]-j-1] = "/"
        elif diff < -1:
            for j in range(-diff):
                column[ypos[i]+j] = "|"
                column[ypos[i]+j+1] = "\\"
        else:
            pass

        for j in range(10):
            graph[j].append(column[j])

    for i in range(len(graph)):
        graph[i].insert(0, "| ")
        graph[i] = "".join(graph[i])
    
    graph.append("+"+"-"*(len(graph[i])-1))

    graph = "\n".join(graph)
    return graph