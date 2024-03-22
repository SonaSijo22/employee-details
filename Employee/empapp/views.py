from django.shortcuts import render,redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee
from django.views.generic import View


# Create your views here.

# Add employee
# ----------------

class EmpAddView(View):
  def get(self,request,*args, **kwargs):
    form=EmployeeForm()
    return render(request,"emp_add.html",{'form':form})

  def post(self,request,*args, **kwargs):   #movie cretae view methodilae post method work chayyan vendi
    form=EmployeeForm(request.POST,files=request.FILES)
    
    if form.is_valid():
      # form.save()
      data=form.cleaned_data
      Employee.objects.create(**data)
      return redirect("emp-list")   #redirect chayyan vendi use chayyunnu add movies pageil ninnu movies all pagesilekku ponam
    return render(request,"emp_add.html",{"form":form})

# list employee
# ------------

class EmployeeListView(View):
  def get(self,request,*args, **kwargs):
    qs=Employee.objects.all()
    return render(request,'emp_list.html',{'data':qs})

# >>delete employees
# ------------------
class EmployeeDeleteView(View):
  def get(self,request,*args, **kwargs):
    id=kwargs.get("pk") 
    Employee.objects.get(id=id).delete()
    return redirect("emp-list")


# >>update employee
# -------------------
class EmployeeUpdateView(View):
  def get(self,request,*args, **kwargs):
    id=kwargs.get("pk")
    emp_object=Employee.objects.get(id=id)
    form=EmployeeForm(instance=emp_object)  
    return render(request,"emp_edit.html",{"form":form})
  # for updatiung we use post method

  def post(self,request,*args, **kwargs):
    # data=request.POST
    id=kwargs.get("pk")
    emp_object=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,files=request.FILES,instance=emp_object)
    if form.is_valid():
      form.save()
      # data=form.cleaned_data
      # Movie.objects.filter(id=id).update(**data)
      return redirect("emp-list")
    else:
      return render(request,"emp_edit.html",{"form":form})

# >>Detail of employees
# --------------------
class EmployeeDetailView(View):
  def get(self,request,*args, **kwargs):
    print(kwargs)#kwargs={"pk":6}
    id=kwargs.get("pk")#pk for primary key
    qs=Employee.objects.get(id=id)
    return render(request,"emp_detail.html",{"data":qs})
