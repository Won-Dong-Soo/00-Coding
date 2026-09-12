<% String x_str=request.getParameter("x"); String y_str=request.getParameter("y"); int result=0; if ((x_str !=null &&
    !"".equals(x_str)) && (y_str !=null && !"".equals(y_str))) { int x=Integer.parseInt(x_str); int
    y=Integer.parseInt(y_str); result=x + y; out.println("result : " + Integer.toString(result));
    }
%>
<hr>
<form action = " plus.jsp" method="GET">
    x : <input type="text" name="x"><br>
    y : <input type="text" name="y"><br>
    <input type="submit">
    </form>