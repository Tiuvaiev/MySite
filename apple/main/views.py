from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'main/index.html', context)


def store(request):
    return render(request, 'main/store.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def repair(request):
    return render(request, 'main/repair.html')


def repair_iphone(request):
    return render(request, 'main/repair_iPhone.html')


def repair_ipad(request):
    return render(request, 'main/repair_iPad.html')


def repair_ipod(request):
    return render(request, 'main/repair_iPod.html')


def repair_macbook(request):
    return render(request, 'main/repair_MacBook.html')


def repair_watch(request):
    return render(request, 'main/repair_Watch.html')


def repair_imac(request):
    return render(request, 'main/repair_iMac.html')

# IPHONE 14 ------------------------------------------------>


def repair_14ProMax(request):
    return render(request, 'main/repair_iPhone/14ProMax.html')


def repair_14Pro(request):
    return render(request, 'main/repair_iPhone/14Pro.html')


def repair_14Plus(request):
    return render(request, 'main/repair_iPhone/14Plus.html')


def repair_14(request):
    return render(request, 'main/repair_iPhone/14.html')

# IPHONE 13 ------------------------------------------------>


def repair_13ProMax(request):
    return render(request, 'main/repair_iPhone/13ProMax.html')


def repair_13Pro(request):
    return render(request, 'main/repair_iPhone/13Pro.html')


def repair_13(request):
    return render(request, 'main/repair_iPhone/13.html')


def repair_13Mini(request):
    return render(request, 'main/repair_iPhone/13Mini.html')

# IPHONE 12 ------------------------------------------------>


def repair_12ProMax(request):
    return render(request, 'main/repair_iPhone/12ProMax.html')


def repair_12Pro(request):
    return render(request, 'main/repair_iPhone/12Pro.html')


def repair_12(request):
    return render(request, 'main/repair_iPhone/12.html')


def repair_12Mini(request):
    return render(request, 'main/repair_iPhone/12Mini.html')

# IPHONE 11 ------------------------------------------------>


def repair_11ProMax(request):
    return render(request, 'main/repair_iPhone/11ProMax.html')


def repair_11Pro(request):
    return render(request, 'main/repair_iPhone/11Pro.html')


def repair_11(request):
    return render(request, 'main/repair_iPhone/11.html')

# IPHONE XsMax,Xs,Xr,X ------------------------------------------------>


def repair_XsMax(request):
    return render(request, 'main/repair_iPhone/XsMax.html')


def repair_Xs(request):
    return render(request, 'main/repair_iPhone/Xs.html')


def repair_Xr(request):
    return render(request, 'main/repair_iPhone/Xr.html')


def repair_X(request):
    return render(request, 'main/repair_iPhone/X.html')

# IPHONE SE/SE2 ------------------------------------------------>


def repair_SE(request):
    return render(request, 'main/repair_iPhone/SE.html')


def repair_SE2(request):
    return render(request, 'main/repair_iPhone/SE2.html')

# IPHONE 8/8Plus ------------------------------------------------>


def repair_8Plus(request):
    return render(request, 'main/repair_iPhone/8Plus.html')


def repair_8(request):
    return render(request, 'main/repair_iPhone/8.html')

# IPHONE 7/7Plus ------------------------------------------------>


def repair_7Plus(request):
    return render(request, 'main/repair_iPhone/7Plus.html')


def repair_7(request):
    return render(request, 'main/repair_iPhone/7.html')

# IPHONE 6sPlus/6s ------------------------------------------------>


def repair_6sPlus(request):
    return render(request, 'main/repair_iPhone/6sPlus.html')


def repair_6s(request):
    return render(request, 'main/repair_iPhone/6s.html')

# IPHONE 6Plus/6 ------------------------------------------------>


def repair_6Plus(request):
    return render(request, 'main/repair_iPhone/6Plus.html')


def repair_6(request):
    return render(request, 'main/repair_iPhone/6.html')

# IPHONE 5s/5c ------------------------------------------------>


def repair_5s(request):
    return render(request, 'main/repair_iPhone/5s.html')


def repair_5c(request):
    return render(request, 'main/repair_iPhone/5c.html')

