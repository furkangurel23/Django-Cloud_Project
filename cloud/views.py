from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.db.models import Count
from .models import (tbl_user, tbl_file, tbl_image,
	tbl_music,
	tbl_video,
	tbl_folder,
	tbl_folder_file,
	tbl_address,tbl_contact,tbl_groups,
	User,
	tbl_share_with_user,
	tbl_groups_user)



@login_required
def home(request):

	num_groups = tbl_groups.objects.all().count()
	num_files = tbl_file.objects.all().count()

	# Available books (status = 'a')
	num_folder = tbl_folder_file.objects.count()

	# The 'all()' is implied by default.
	num_shared = tbl_share_with_user.objects.count()
	# Number of visits to this view, as counted in the session variable.
	num_visits = request.session.get('num_visits', 0)
	request.session['num_visits'] = num_visits + 1

	context = {
		'num_groups': num_groups,
		'num_files': num_files,
		'num_folder': num_folder,
		'num_shared': num_shared,
		'num_visits': num_visits,
	}

	"""context ={
		'folders':tbl_folder.objects.all()

	}"""
	return render(request, 'cloud/home.html', context)

def register(request):
	if request.method =='POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your account has been created! You are now able to log in')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'cloud/register.html', {'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.tbl_user)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance = request.user)
		p_form = ProfileUpdateForm(instance = request.user.tbl_user)
	context = {
		'u_form' : u_form,
		'p_form' : p_form
	}
	return render(request, 'cloud/profile.html', context) 

def file(request):
	context= {
		'folders': tbl_folder.objects.all(),
		'files':tbl_file.objects.all()
	}
	return render(request, 'cloud/tbl_folder_list.html', context)

def contacts(request):
	context = {
		'contacts':tbl_contact.objects.all(),
	}
	return render(request,'cloud/tbl_contact_list.html',context)
def groups(request):
	context={
		'groups':tbl_groups.objects.all()
	}
	return render(request,'cloud/tbl_groups_list.html',context)


class FileDetailView(generic.DetailView):
	model = tbl_file
	"""def get_object(self):
	        pk1 = self.kwargs['pk1']
	        pk2 = self.kwargs['pk2']
	        folder = get_object_or_404(tbl_folder, pk=pk1)
	        file = get_object_or_404(tbl_file, pk=pk2)
	        return file"""

class ContactDetailView(generic.DetailView):
	model = tbl_contact
class GroupDetailView(generic.DetailView):
	model = tbl_groups
class GroupUserDetailView(generic.DetailView):
	model = tbl_groups_user
class UserDetailView(generic.DetailView):
	model = User
class SharedFileDetailView(generic.DetailView):
	model = tbl_share_with_user

class FolderDetailView(generic.DetailView):
	model = tbl_folder

class FolderListView(generic.ListView):
    model = tbl_folder

class FolderCreateView(LoginRequiredMixin, CreateView):
	model = tbl_folder
	fields = ['parent_folder' ,'title', 'describtion', 'size', 'isFav']

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class FolderUpdateView(LoginRequiredMixin, UpdateView):
	model = tbl_folder
	fields = ['parent_folder' ,'title', 'describtion', 'size', 'isFav']
	success_url='/'

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

	"""def test_func(self): # cok gerekli olmaya bir sey
		folder = self.get_object()
		if self.request.user.tbl_user == folder.owner_id: 
			return True
		return False"""

class FolderDeleteView(LoginRequiredMixin, DeleteView):
    model = tbl_folder
    success_url ='/'
    """def test_func(self): # cok gerekli olmaya bir sey
		folder = self.get_object()
		if self.request.user.tbl_user == folder.owner_id: 
			return True
		return False"""
class FileCreateView(CreateView):
	model = tbl_file
	fields =['title','isFav','size']
	#success_url='file/new/new/'
	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class FileFolderCreate(CreateView):
	model = tbl_folder_file
	fields = ['folder_id','file_id']
	success_url = '/'

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class FileUpdateView(LoginRequiredMixin, UpdateView):
	model = tbl_file
	fields = ['title','isFav','size']
	#success_url='/'

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class FileDeleteView(LoginRequiredMixin, DeleteView):
    model = tbl_file
    success_url ='/'

class ContactCreateView(CreateView):
	model = tbl_contact
	fields =['owner_id','full_name','e_mail','phone_number','location','from_next_cloud_or_another']

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class ContactDeleteView(DeleteView):
	model = tbl_contact
	success_url ='/'

class ShareCreateView(CreateView):
	model = tbl_share_with_user
	fields = ['file_id', 'user_id', 'user_id2', 'expire_on', 'readable_writable']
	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class GroupCreateView(CreateView):
	model = tbl_groups
	fields = ['group_name', 'isAdmin']

	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)

class FillGroupView(CreateView):
	model = tbl_groups_user
	fields = ['group_id', 'user_id'] 
	success_url = '/'
	def form_valid(self, form):
		#form.instance.Owner = self.request.user
		form.instance.owner_id = self.request.user.tbl_user
		return super().form_valid(form)
