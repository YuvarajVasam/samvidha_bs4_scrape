from bs4 import BeautifulSoup 
html_content = """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>IARE -  - Student</title>
	<!-- Favicons -->
	<link href="https://samvidha.iare.ac.in/images/favicon.ico" rel="icon">
	<!-- Tell the browser to be responsive to screen width -->
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Font Awesome -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/fontawesome-free/css/all.min.css">
	<!-- Ionicons -->
	<link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
	<!-- Tempusdominus Bbootstrap 4 -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
	<!-- iCheck -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/icheck-bootstrap/icheck-bootstrap.min.css">
	<!-- JQVMap -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/jqvmap/jqvmap.min.css">
	<!-- Theme style -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/dist/css/adminlte.min.css" >
	<!-- overlayScrollbars -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
	<!-- Daterange picker -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/daterangepicker/daterangepicker.css">
	<!-- summernote -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/summernote/summernote-bs4.css">
	<!-- Google Font: Source Sans Pro -->
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700" rel="stylesheet">
	<!-- my Custome style -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/dist/css/custome.css">
	
	<!-- jQuery -->
	<script src="https://samvidha.iare.ac.in/plugins/jquery/jquery.min.js"></script>
	<!-- jQuery UI 1.11.4 -->
	<script src="https://samvidha.iare.ac.in/plugins/jquery-ui/jquery-ui.min.js"></script>
	<!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
	<!-- Bootstrap 4 -->
	<script src="https://samvidha.iare.ac.in/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
	<!-- SweetAlert2 -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/sweetalert2-theme-bootstrap-4/bootstrap-4.min.css">
	<script src="https://samvidha.iare.ac.in/plugins/sweetalert2/sweetalert2.min.js"></script>
	
	
</head>
<body class="hold-transition sidebar-mini layout-fixed sidebar-collapse">

<div class="wrapper"> 
<!-- Navbar -->
  <nav class="main-header navbar navbar-expand navbar-white navbar-light">
    <!-- Left navbar links -->
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="https://samvidha.iare.ac.in/home" class="nav-link">Home</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="#" class="nav-link">Contact</a>
      </li>
	  <li class="nav-item d-none d-sm-inline-block">
        <a href="https://samvidha.iare.ac.in/logout" class="nav-link text-danger">Sign out</a>
      </li>
	  
    </ul>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      <!-- Notifications Dropdown Menu -->
      <li class="nav-item dropdown">
        <a class="nav-link" data-toggle="dropdown" href="#">
          <i class="far fa-bell"></i>
          <span class="badge badge-warning navbar-badge">0</span>
        </a>
        <!--<div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <span class="dropdown-item dropdown-header">15 Notifications</span>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-envelope mr-2"></i> 4 new messages
            <span class="float-right text-muted text-sm">3 mins</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-users mr-2"></i> 8 requests
            <span class="float-right text-muted text-sm">12 hours</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-file mr-2"></i> 3 new reports
            <span class="float-right text-muted text-sm">2 days</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item dropdown-footer">See All Notifications</a>
        </div>-->
      </li>
	  <li class="nav-item dropdown user user-menu open">
		 <a class="nav-link" data-toggle="dropdown" href="#">
						<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/22951A66J6.jpg" class="user-image" title="VASAM YUVARAJ">
			<span class="hidden-xs">VASAM YUVARAJ</span>
		</a>
		<ul class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
		  <!-- User image -->
		  <li class="user-header">
			<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/22951A66J6.jpg" class="img-circle" alt="VASAM YUVARAJ" title="VASAM YUVARAJ">
			<p>VASAM YUVARAJ</p>
			<small>
			22951A66J6<br/>B.Tech IV Semester - C Section<br/>Computer Science and Engineering (AI & ML)			</small>
		  </li>
		  <!-- Menu Footer-->
		  <li class="user-footer">
						<div class="float-left">
			  <a href="https://samvidha.iare.ac.in/home?action=profile" class="btn btn-primary">Profile</a>
			</div>
						<div class="float-right">
			  <a href="https://samvidha.iare.ac.in/logout" class="btn btn-danger">Sign out</a>
			</div>
		  </li>
		</ul>
	  </li>
	  
    
    </ul>
  </nav>
  <!-- /.navbar --><!-- Main Sidebar Container -->
<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="https://samvidha.iare.ac.in/home" class="brand-link" title="Institute of Aeronautical Engineering">
		<img src="https://samvidha.iare.ac.in/images//logo.jpg" alt="Institute of Aeronautical Engineering" title="Institute of Aeronautical Engineering" class="brand-image img-circle elevation-3">
		<span class="brand-text font-weight-light">IARE</span>
    </a>
	<!-- Sidebar -->
    <div class="sidebar">
		<!-- Sidebar Menu -->
		<nav class="mt-2">
			<input type="text" id="myInput" placeholder="Search for menu.." title="Type in a menu name">
			<ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
				<!-- Add icons to the links using the .nav-icon class with font-awesome or any other icon font library -->
				<li class="nav-item">
					<a href="https://samvidha.iare.ac.in/home" class="nav-link " title="Dashboard">
						<i class="nav-icon fas fa-tachometer-alt"></i>
						<p> Dashboard </p>
					</a>
				</li>
										<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Examinations">
								  <i class="nav-icon fas fa-graduation-cap"></i>
								  <p>Examinations <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=cie_marks_ug" class="nav-link" title="Continuous Internal Assessment (CIA) Marks">
												  <i class="nav-icon fas far fa-star"></i>
												  <p> CIA Marks </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=admit_card_std" class="nav-link" title="Admit Card">
												  <i class="nav-icon fas fa-print"></i>
												  <p> Admit Card </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=exam_registration" class="nav-link" title="Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Exam Registration </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=makeupexam_registration" class="nav-link" title="Makeup Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Makeup Exam Registration </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=exam_results" class="nav-link" title="Exam Result">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Exam Result </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=credit_register" class="nav-link" title="Credit Register">
												  <i class="nav-icon fas "></i>
												  <p> Credit Register </p>
												</a>
											</li>
																				<li class="nav-item has-treeview">
												<a href="#" class="nav-link" title="Booklets">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p>Booklets <i class="fas fa-angle-left right"></i></p>
												</a>
												<ul class="nav nav-treeview">
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=see_booklet" class="nav-link" title="SEE Booklets">
																  <i class="nav-icon fas "></i>
																  <p> SEE Booklets </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=cie_booklet" class="nav-link" title="CIE Booklets">
																  <i class="nav-icon fas "></i>
																  <p> CIE Booklets </p>
																</a>
															</li>
																									</ul>
											</li>
																					<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=qp_scheme" class="nav-link" title="Question Paper and Solution">
												  <i class="nav-icon fas fa-question"></i>
												  <p> Question Paper and Solution </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=revaluation" class="nav-link" title="Revaluation">
												  <i class="nav-icon fas fa-recycle"></i>
												  <p> Revaluation </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=rem_registration" class="nav-link" title="Remedial Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Remedial Exam Registration </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Academics">
								  <i class="nav-icon fas fa-university"></i>
								  <p>Academics <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=course_content" class="nav-link" title="Course Content Delivery">
												  <i class="nav-icon fas fa-heart"></i>
												  <p> Course Content Delivery </p>
												</a>
											</li>
																				<li class="nav-item has-treeview">
												<a href="#" class="nav-link" title="Course Registration">
												  <i class="nav-icon fas fa-registered"></i>
												  <p>Course Registration <i class="fas fa-angle-left right"></i></p>
												</a>
												<ul class="nav nav-treeview">
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=Course_Reg" class="nav-link" title="Regular Course Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Regular Courses </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=Acc_Course_Reg" class="nav-link" title="Accelerated Course Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Accelerated Courses </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=honor_course" class="nav-link" title="Honors Program Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Honors </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=minor" class="nav-link" title="Minors Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Minors </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=lite_course_std" class="nav-link" title="AICTE LITE Program Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> AICTE LITE Program Registration </p>
																</a>
															</li>
																									</ul>
											</li>
																					<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=stud_att_STD" class="nav-link" title="Attendance">
												  <i class="nav-icon fas  fa-registered"></i>
												  <p> Attendance </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=Attendance_std" class="nav-link" title="PAT Attendance">
												  <i class="nav-icon fas fa-handshake"></i>
												  <p> PAT Attendance </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=std_att_register" class="nav-link" title="Attendance Register">
												  <i class="nav-icon fas fa-hand-point-left"></i>
												  <p> Attendance Register </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=proj_title_allotment" class="nav-link" title="Project Selection & Allotment">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Selection & Allotment </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=aat_qst_select_std" class="nav-link" title="AAT Question Selection">
												  <i class="nav-icon fas fa-plus"></i>
												  <p> AAT Question Selection </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=tm_allotment" class="nav-link" title="Project Team Member Selection">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Team Member Selection </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=prj_thesis_report_STD" class="nav-link" title="Project Work /Thesis Report">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Work /Thesis Report </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Requisitions">
								  <i class="nav-icon fas fa-graduation-cap"></i>
								  <p>Requisitions <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=req_certificate" class="nav-link" title="Certificate Request">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Certificate Request </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=req_trans_stud" class="nav-link" title="Transcript / Duplicate / Name Correction Memo">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Transcript / Duplicate / Name Correction Memo </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=skill_reg_frm" class="nav-link" title="Skill Program">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Skill Program </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Print Forms">
								  <i class="nav-icon fas fa-print"></i>
								  <p>Print Forms <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=print_no_due" class="nav-link" title="No Dues">
												  <i class="nav-icon fas fa-print"></i>
												  <p> No Dues </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=print_tc_due" class="nav-link" title="TC Form">
												  <i class="nav-icon fas fa-print"></i>
												  <p> TC Form </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=acc_register_std" class="nav-link " title="Accession Register">
								  <i class="nav-icon fas fa-hand-point-left"></i>
								  <p> Accession Register </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=workshop_Registration" class="nav-link " title="2023 MCUT-IARE ONLINE WORKSHOP">
								  <i class="nav-icon fas fa-registered"></i>
								  <p> 2023 MCUT- IARE ONLINE WORKSHOP Registration </p>
								</a>
							</li>
													<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Payments">
								  <i class="nav-icon fas fa-money-bill"></i>
								  <p>Payments <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment" class="nav-link" title="Online Fees Payment">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Online Fees Payment </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment_ccav" class="nav-link" title="Online Fees Payment CCAV">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Online Fees Payment CCAV </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment_status" class="nav-link" title="Fee Status">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Fee Status </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=BC_STD" class="nav-link " title="Bonafide Certificate">
								  <i class="nav-icon fas fa-money-bill"></i>
								  <p> Bonafide Certificate </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=TT_std" class="nav-link " title="Timetable">
								  <i class="nav-icon fas fa-hand-point-left"></i>
								  <p> Timetable </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=mybox" class="nav-link " title="My Box">
								  <i class="nav-icon fas fa-inbox"></i>
								  <p> My Box </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=bus_registration" class="nav-link " title="">
								  <i class="nav-icon fas fa-registered"></i>
								  <p> Bus Registration </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=up_photo_std" class="nav-link " title="Upload Birth Certificate">
								  <i class="nav-icon fas fa-upload"></i>
								  <p> Upload Birth Certificate </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=up_abc_std" class="nav-link " title="Update Academic Bank of credit">
								  <i class="nav-icon fas fa-edit"></i>
								  <p> Update Academic Bank of credit </p>
								</a>
							</li>
													<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Uploads">
								  <i class="nav-icon fas fa-upload"></i>
								  <p>Uploads <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=up_fp_std" class="nav-link" title="Upload Field Project">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Upload Field Project </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=upload_cvn_std" class="nav-link" title="Upload CVC Certificate">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Upload CVC Certificate </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=aat_upload" class="nav-link" title="AAT (Tech Talk / Seminar Talk)">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> AAT (Tech Talk) </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=project_upload" class="nav-link" title="Upload Project Work">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> Upload Project Work </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=upload_aat_2" class="nav-link" title="AAT-II">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> AAT-II </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=labrecord_std" class="nav-link" title="Lab Record">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> Lab Record </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Feedback">
								  <i class="nav-icon fas fa-comment"></i>
								  <p>Feedback <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=esf" class="nav-link" title="Early Semester Feedback">
												  <i class="nav-icon fas "></i>
												  <p> Early Semester Feedback </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=obe_fb_std" class="nav-link" title="OBE Feedback">
												  <i class="nav-icon fas "></i>
												  <p> OBE Feedback </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=std_review_syllabus" class="nav-link" title="Design and Review of Syllabus">
												  <i class="nav-icon fas "></i>
												  <p> Design and Review of Syllabus </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=ss_std" class="nav-link" title="Satisfaction Survey">
												  <i class="nav-icon fas "></i>
												  <p> Satisfaction Survey </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=placement_std" class="nav-link" title="Placement Experience">
												  <i class="nav-icon fas "></i>
												  <p> Placement Experience </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=ns" class="nav-link" title="NAAC SURVEY">
												  <i class="nav-icon fas "></i>
												  <p> NAAC SURVEY </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=std_bio" class="nav-link " title="Biometric ">
								  <i class="nav-icon fas fa-fingerprint"></i>
								  <p> Biometric </p>
								</a>
							</li>
									</ul>
		</nav>
      <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
  </aside>
<style>
#myInput {
  background-image: url('/images/searchicon.png');
  background-position:10px 3px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding:3px 20px 3px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>
<script>
  var parent = $("ul.sidebar-menu li.active").closest("ul").closest("li");
  if (parent[0] != undefined)
    $(parent[0]).addClass("active");

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".nav-sidebar li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

</script><!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>profile</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">profile</li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-6">
					<!-- Profile Image -->
					<div class="card card-primary card-outline">
						<div class="card-body box-profile">
							<div class="text-center">
																<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/22951A66J6.jpg" class="profile-user-img img-fluid img-circle" title="VASAM YUVARAJ" alt="VASAM YUVARAJ">
							</div>
							<h3 class="profile-username text-center">VASAM YUVARAJ</h3>
														<p class="text-muted text-center">Computer Science and Engineering (AI & ML)</p>
						</div>
						<!-- /.card-body -->
					</div>
										<div class="card card-primary">
						<div class="card-header bg-teal btn" data-card-widget="collapse">
							<h3 class="card-title">General</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-4">Roll Number</dt>
								<dd class="col-sm-8">22951A66J6</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">ABC ID</dt>
								<dd class="col-sm-8">895-746-531-651</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">JNTUH AEBAS</dt>
								<dd class="col-sm-8">218129-23036</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Name</dt>
								<dd class="col-sm-8">VASAM YUVARAJ</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">AAdhar Number</dt>
								<dd class="col-sm-8">9962 2545 4409</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Branch</dt>
								<dd class="col-sm-8">Computer Science and Engineering (AI & ML)</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Year/Sem</dt>
								<dd class="col-sm-8">II B.Tech II Sem</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Section</dt>
								<dd class="col-sm-8">C</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Gender</dt>
								<dd class="col-sm-8">M</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Name</dt>
								<dd class="col-sm-8">VASAM SHIVA PRASAD</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Mother Name</dt>
								<dd class="col-sm-8">VASEM KAVITHA</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Occupation Type</dt>
								<dd class="col-sm-8">Other</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Occupation</dt>
								<dd class="col-sm-8">DAILY LABOUR</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Date of Birth</dt>
								<dd class="col-sm-8">30-08-2004</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Date of Joining</dt>
								<dd class="col-sm-8">28-10-2022</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Regulation</dt>
								<dd class="col-sm-8">R20</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Status</dt>
								<dd class="col-sm-8">Studying</dd>
								
							</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-lightblue btn" data-card-widget="collapse">
							<h3 class="card-title ">Contacts</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<strong><i class="fas fa-lg fa-building mr-1"></i> Present Address</strong>
							<p class="text-muted">H.NO: 1-2-108, KORATLA, JAGITHYAL, TELANGANA- 505326</p>
							<hr>
							<strong><i class="fas fa-lg fa-building mr-1"></i> Permanent Address</strong>
							<p class="text-muted">H.NO: 1-2-108, KORATLA, JAGITHYAL, TELANGANA- 505326</p>
							<hr>
							<strong><i class="fas fa-phone mr-1"></i> Student Phone</strong>
							<p class="text-muted">9490244911</p>
							<hr>
							<strong><i class="fas fa-phone mr-1"></i> Parent Phone</strong>
							<p class="text-muted">9492984416</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Student Email-id</strong>
							<p class="text-muted">yuvarajvasam03@gmail.com</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Parent Email-id</strong>
							<p class="text-muted">vasamshivaprasad464@gmail.com</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Domain Email-id</strong>
							<p class="text-muted">22951A66J6@iare.ac.in</p>
													</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="card card-primary">
						<div class="card-header bg-pink btn" data-card-widget="collapse">
							<h3 class="card-title ">Administrative Information</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<!-- /.card-header -->
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-4">Admission No</dt>
								<dd class="col-sm-8">8850</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">EAMCET RANK</dt>
								<dd class="col-sm-8">19157</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Admission Type</dt>
								<dd class="col-sm-8">Convenor</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Tuition Fee</dt>
								<dd class="col-sm-8">101000</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Tuition Fee Waiver Amount</dt>
								<dd class="col-sm-8">35000</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">PHC</dt>
								<dd class="col-sm-8">N</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Fee Category</dt>
								<dd class="col-sm-8">FEE-EXEMPTED</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Caste Category</dt>
								<dd class="col-sm-8">BC-B</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Region</dt>
								<dd class="col-sm-8">OU</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Religion</dt>
								<dd class="col-sm-8">HINDU</dd>
							</dl>
						</div>
						<!-- /.card-body -->
					</div>
					<!-- /.card -->
					<div class="card card-primary">
						<div class="card-header bg-teal" data-card-widget="collapse">
							<h3 class="card-title ">Marks Details</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-8">SSC Percentage/CBSE</dt>
								<dd class="col-sm-4">10.00</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-8">Inter Percentage/Diploma</dt>
								<dd class="col-sm-4">92.50</dd>
																<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-8">Degree Percentage</dt>
								<dd class="col-sm-4"></dd>
															</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-orange " data-card-widget="collapse">
							<h3 class="card-title ">Academic Progress</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">		
																<dt class="col-sm-4">I B.Tech</dt>
									<dd class="col-sm-8">Promoted to Next Semester</dd>
								 
									<div class="col-sm-12 dropdown-divider"></div>
																	<dt class="col-sm-4">II B.Tech I Sem</dt>
									<dd class="col-sm-8">Promoted to Next Semester</dd>
								 
									<div class="col-sm-12 dropdown-divider"></div>
																	<dt class="col-sm-4">II B.Tech II Sem</dt>
									<dd class="col-sm-8">Studying</dd>
															</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-success">
							<h3 class="card-title ">Disciplinay Actions</h3>
						</div>
					</div>
					<div class="card card-lightblue" >
						<div class="card-header bg-lightblue" data-card-widget="collapse">
							<h3 class="card-title">Group Personal Accident Policy</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body p-0">
							<table class="table table-striped table-hover">
								<thead>
									<tr>
										<th style="width: 10px">S.no</th>
										<th>AY</th>
										<th>Status</th>
										<th>View</th>
									</tr>
								</thead>
																<tbody>
																				<tr>
												<td>1</td>
												<td>Group Personal Accident Policy - 2023-24</td>
												<td>Active</td>
												<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/Group_Policy/Student_2023-24.pdf' data-type="pdf" class="btn btn-sm bg-maroon display" target='_BLANK' alt="Group Personal Accident Policy" title="Group Personal Accident Policy"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></a></td>
											</tr>
																	</tbody>
							</table>
						</div>
					</div>
					<div class="card card-lightblue" >
						<div class="card-header bg-lightblue" data-card-widget="collapse">
							<h3 class="card-title">Certificates List</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body p-0">
							<table class="table table-striped table-hover">
								<thead>
									<tr>
										<th style="width: 10px">S.no</th>
										<th>Certificate</th>
										<th>View</th>
									</tr>
								</thead>
								<tbody>
																			<tr>
											<td>2</td>
											<td>SSC CERTIFICATE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_SSC.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>3</td>
											<td>INTER CERTIFICATE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_INTER.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>4</td>
											<td>AADHAR</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Aadhar.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>5</td>
											<td>Income Certificate</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Income.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>6</td>
											<td>Caste Certificate</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_Caste.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>7</td>
											<td>Prev Institue TransferCerticate</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_TC.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>8</td>
											<td>SSC/INTER/UG LONG MARKS MEMO</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_MARKSMEMO.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>9</td>
											<td>CET Allotment Order</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_CET_ALLOTMENT_ORDER.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>10</td>
											<td>Joining Report</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_JR.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>11</td>
											<td>INTER BONAFIDE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_INTER_BONAFIDE.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>12</td>
											<td>SSC BONAFIDE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_SSC_BONAFIDE.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>13</td>
											<td>EAMCET/ECET/ICET/PGCET RANK</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_EAMCET_RANK.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>14</td>
											<td>SCHOOL BONAFIDE 1</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_SCHOOL_BC_1.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>15</td>
											<td>EAMCET/ECET/ICET/PGCET Hall Ticket</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/DOCS/22951A66J6_CET_HALLTICKET.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																	</tbody>
							</table>
						</div>
					</div>
				</div>
				<div class="col-md-12">
										<div class="bg-success">
						<h4 class="text-center">Overall Conduct is GOOD</h4>
					</div>
				</div>
			</div>
        <!-- /.row -->
		</div><!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>
<div class="modal fade" id="modal-update_project">
	<div class="modal-dialog modal-xl">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close btn btn-danger" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<div class="col-sm-12 mgauto dataTables_wrapper">
					<img src="" id="img_doc" width="100%" height="600" style="border: none;"/>
					<iframe id="fram_doc" src="" width="100%" height="600" style="border: none;"></iframe>
				</div>
			</div>
			<div class="modal-footer justify-content-between">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
			</div>
		</div>
		<!-- /.modal-content -->
	</div>
	<!-- /.modal-dialog -->
</div>
<script type="text/javascript">
	$(document).ready(function () {
		$(".display").click(function(e){
			e.preventDefault();
			if($(this).data("type") == 'pdf'){
				$('#fram_doc').attr('src',$(this).attr("href")+"#toolbar=0&amp;navpanes=0&amp;scrollbar=0");
				$('#fram_doc').show();
				$('#img_doc').hide();
			}else if($(this).data("type") == 'jpg'){
				$('#fram_doc').hide();
				$('#img_doc').attr('src',$(this).attr("href"));
				$('#img_doc').show();
			}
			$('#modal-update_project').modal({backdrop: 'static', keyboard: false},'show');
		});
	});
</script></div>
<footer class="main-footer">
  <strong>Copyright &copy; 2024  Institute of Aeronautical Engineering.</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All rights reserved.
</footer>
	
	


<!-- ChartJS -->
<script src="https://samvidha.iare.ac.in/plugins/chart.js/Chart.min.js"></script>

<!-- Sparkline -->
<script src="https://samvidha.iare.ac.in/plugins/sparklines/sparkline.js"></script>

<!-- jQuery Knob Chart -->
<script src="https://samvidha.iare.ac.in/plugins/jquery-knob/jquery.knob.min.js"></script>
<!-- daterangepicker -->
<script src="https://samvidha.iare.ac.in/plugins/moment/moment.min.js"></script>
<script src="https://samvidha.iare.ac.in/plugins/daterangepicker/daterangepicker.js"></script>
<!-- Bootstrap Switch -->
<script src="https://samvidha.iare.ac.in/plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script>
<!-- Tempusdominus Bootstrap 4 -->
<script src="https://samvidha.iare.ac.in/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
<!-- Summernote -->
<script src="https://samvidha.iare.ac.in/plugins/summernote/summernote-bs4.min.js"></script>
<!-- overlayScrollbars -->
<script src="https://samvidha.iare.ac.in/plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
<!-- AdminLTE App -->
<script src="https://samvidha.iare.ac.in/dist/js/adminlte.js"></script>

<!-- AdminLTE for demo purposes -->
<script src="https://samvidha.iare.ac.in/dist/js/demo.js"></script>
	<script>
	$(document).ready(function(){  
		function check_session(){
			$.ajax({
				url:"pages/layout/check_session.php",
				method:"POST",
				success:function(data)
				{
					if(data == '1')
					{
						//alert('Your session has been expired!');  
						window.location.href="index";
					}
				}
			})
		}
		setInterval(function(){
			check_session();
		}, 60000);  //60000 means 60 seconds
	});  
	$("html").on("contextmenu",function(e){
		return false;
    });
	$('#fram_doc').bind('contextmenu',function(e){ 
		return false; 
	});
	
	$(document).bind("menubar",function(e) {
		//e.preventDefault();
	});
	
	$(document).keydown(function(e){
		
		if(e.ctrlKey && e.keyCode == 83){
			e.preventDefault(); 
			return false;
		}
		if(e.which === 123 || e.which === 17 || e.which === 18 || e.which === 16){
		   e.preventDefault(); 
		   return false;
		}
		if ((e.ctrlKey && e.shiftKey && e.keyCode == 73) || (e.ctrlKey && e.keyCode==73) || (e.ctrlKey && e.shiftKey && e.keyCode == 74)  || (e.altKey && e.keyCode == 70)) {
			 e.preventDefault(); 
			return false;
		}
		//alert(e.keyCode);
	
	});
	
	
  $.widget.bridge('uibutton', $.ui.button)
</script></body>
</html>

"""

html_content_2 = """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>IARE -  - Student</title>
	<!-- Favicons -->
	<link href="https://samvidha.iare.ac.in/images/favicon.ico" rel="icon">
	<!-- Tell the browser to be responsive to screen width -->
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Font Awesome -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/fontawesome-free/css/all.min.css">
	<!-- Ionicons -->
	<link rel="stylesheet" href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css">
	<!-- Tempusdominus Bbootstrap 4 -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/tempusdominus-bootstrap-4/css/tempusdominus-bootstrap-4.min.css">
	<!-- iCheck -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/icheck-bootstrap/icheck-bootstrap.min.css">
	<!-- JQVMap -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/jqvmap/jqvmap.min.css">
	<!-- Theme style -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/dist/css/adminlte.min.css" >
	<!-- overlayScrollbars -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/overlayScrollbars/css/OverlayScrollbars.min.css">
	<!-- Daterange picker -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/daterangepicker/daterangepicker.css">
	<!-- summernote -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/summernote/summernote-bs4.css">
	<!-- Google Font: Source Sans Pro -->
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700" rel="stylesheet">
	<!-- my Custome style -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/dist/css/custome.css">
	
	<!-- jQuery -->
	<script src="https://samvidha.iare.ac.in/plugins/jquery/jquery.min.js"></script>
	<!-- jQuery UI 1.11.4 -->
	<script src="https://samvidha.iare.ac.in/plugins/jquery-ui/jquery-ui.min.js"></script>
	<!-- Resolve conflict in jQuery UI tooltip with Bootstrap tooltip -->
	<!-- Bootstrap 4 -->
	<script src="https://samvidha.iare.ac.in/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
	<!-- SweetAlert2 -->
	<link rel="stylesheet" href="https://samvidha.iare.ac.in/plugins/sweetalert2-theme-bootstrap-4/bootstrap-4.min.css">
	<script src="https://samvidha.iare.ac.in/plugins/sweetalert2/sweetalert2.min.js"></script>
	
	
</head>
<body class="hold-transition sidebar-mini layout-fixed sidebar-collapse">

<div class="wrapper"> 
<!-- Navbar -->
  <nav class="main-header navbar navbar-expand navbar-white navbar-light">
    <!-- Left navbar links -->
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" data-widget="pushmenu" href="#" role="button"><i class="fas fa-bars"></i></a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="https://samvidha.iare.ac.in/home" class="nav-link">Home</a>
      </li>
      <li class="nav-item d-none d-sm-inline-block">
        <a href="#" class="nav-link">Contact</a>
      </li>
	  <li class="nav-item d-none d-sm-inline-block">
        <a href="https://samvidha.iare.ac.in/logout" class="nav-link text-danger">Sign out</a>
      </li>
	  
    </ul>

    <!-- Right navbar links -->
    <ul class="navbar-nav ml-auto">
      <!-- Notifications Dropdown Menu -->
      <li class="nav-item dropdown">
        <a class="nav-link" data-toggle="dropdown" href="#">
          <i class="far fa-bell"></i>
          <span class="badge badge-warning navbar-badge">0</span>
        </a>
        <!--<div class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
          <span class="dropdown-item dropdown-header">15 Notifications</span>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-envelope mr-2"></i> 4 new messages
            <span class="float-right text-muted text-sm">3 mins</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-users mr-2"></i> 8 requests
            <span class="float-right text-muted text-sm">12 hours</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item">
            <i class="fas fa-file mr-2"></i> 3 new reports
            <span class="float-right text-muted text-sm">2 days</span>
          </a>
          <div class="dropdown-divider"></div>
          <a href="#" class="dropdown-item dropdown-footer">See All Notifications</a>
        </div>-->
      </li>
	  <li class="nav-item dropdown user user-menu open">
		 <a class="nav-link" data-toggle="dropdown" href="#">
						<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/22951A66F3.jpg" class="user-image" title="BOORLA SWATHI">
			<span class="hidden-xs">BOORLA SWATHI</span>
		</a>
		<ul class="dropdown-menu dropdown-menu-lg dropdown-menu-right">
		  <!-- User image -->
		  <li class="user-header">
			<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/22951A66F3.jpg" class="img-circle" alt="BOORLA SWATHI" title="BOORLA SWATHI">
			<p>BOORLA SWATHI</p>
			<small>
			22951A66F3<br/>B.Tech IV Semester - C Section<br/>Computer Science and Engineering (AI & ML)			</small>
		  </li>
		  <!-- Menu Footer-->
		  <li class="user-footer">
						<div class="float-left">
			  <a href="https://samvidha.iare.ac.in/home?action=profile" class="btn btn-primary">Profile</a>
			</div>
						<div class="float-right">
			  <a href="https://samvidha.iare.ac.in/logout" class="btn btn-danger">Sign out</a>
			</div>
		  </li>
		</ul>
	  </li>
	  
    
    </ul>
  </nav>
  <!-- /.navbar --><!-- Main Sidebar Container -->
<aside class="main-sidebar sidebar-dark-primary elevation-4">
    <!-- Brand Logo -->
    <a href="https://samvidha.iare.ac.in/home" class="brand-link" title="Institute of Aeronautical Engineering">
		<img src="https://samvidha.iare.ac.in/images//logo.jpg" alt="Institute of Aeronautical Engineering" title="Institute of Aeronautical Engineering" class="brand-image img-circle elevation-3">
		<span class="brand-text font-weight-light">IARE</span>
    </a>
	<!-- Sidebar -->
    <div class="sidebar">
		<!-- Sidebar Menu -->
		<nav class="mt-2">
			<input type="text" id="myInput" placeholder="Search for menu.." title="Type in a menu name">
			<ul class="nav nav-pills nav-sidebar flex-column" data-widget="treeview" role="menu" data-accordion="false">
				<!-- Add icons to the links using the .nav-icon class with font-awesome or any other icon font library -->
				<li class="nav-item">
					<a href="https://samvidha.iare.ac.in/home" class="nav-link " title="Dashboard">
						<i class="nav-icon fas fa-tachometer-alt"></i>
						<p> Dashboard </p>
					</a>
				</li>
										<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Examinations">
								  <i class="nav-icon fas fa-graduation-cap"></i>
								  <p>Examinations <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=cie_marks_ug" class="nav-link" title="Continuous Internal Assessment (CIA) Marks">
												  <i class="nav-icon fas far fa-star"></i>
												  <p> CIA Marks </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=admit_card_std" class="nav-link" title="Admit Card">
												  <i class="nav-icon fas fa-print"></i>
												  <p> Admit Card </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=exam_registration" class="nav-link" title="Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Exam Registration </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=makeupexam_registration" class="nav-link" title="Makeup Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Makeup Exam Registration </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=exam_results" class="nav-link" title="Exam Result">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Exam Result </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=credit_register" class="nav-link" title="Credit Register">
												  <i class="nav-icon fas "></i>
												  <p> Credit Register </p>
												</a>
											</li>
																				<li class="nav-item has-treeview">
												<a href="#" class="nav-link" title="Booklets">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p>Booklets <i class="fas fa-angle-left right"></i></p>
												</a>
												<ul class="nav nav-treeview">
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=see_booklet" class="nav-link" title="SEE Booklets">
																  <i class="nav-icon fas "></i>
																  <p> SEE Booklets </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=cie_booklet" class="nav-link" title="CIE Booklets">
																  <i class="nav-icon fas "></i>
																  <p> CIE Booklets </p>
																</a>
															</li>
																									</ul>
											</li>
																					<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=qp_scheme" class="nav-link" title="Question Paper and Solution">
												  <i class="nav-icon fas fa-question"></i>
												  <p> Question Paper and Solution </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=revaluation" class="nav-link" title="Revaluation">
												  <i class="nav-icon fas fa-recycle"></i>
												  <p> Revaluation </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=rem_registration" class="nav-link" title="Remedial Exam Registration">
												  <i class="nav-icon fas fa-graduation-cap"></i>
												  <p> Remedial Exam Registration </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Academics">
								  <i class="nav-icon fas fa-university"></i>
								  <p>Academics <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=course_content" class="nav-link" title="Course Content Delivery">
												  <i class="nav-icon fas fa-heart"></i>
												  <p> Course Content Delivery </p>
												</a>
											</li>
																				<li class="nav-item has-treeview">
												<a href="#" class="nav-link" title="Course Registration">
												  <i class="nav-icon fas fa-registered"></i>
												  <p>Course Registration <i class="fas fa-angle-left right"></i></p>
												</a>
												<ul class="nav nav-treeview">
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=Course_Reg" class="nav-link" title="Regular Course Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Regular Courses </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=Acc_Course_Reg" class="nav-link" title="Accelerated Course Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Accelerated Courses </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=honor_course" class="nav-link" title="Honors Program Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Honors </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=minor" class="nav-link" title="Minors Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> Minors </p>
																</a>
															</li>
																												<li class="nav-item">
																<a href="https://samvidha.iare.ac.in/home?action=lite_course_std" class="nav-link" title="AICTE LITE Program Registration">
																  <i class="nav-icon fas fa-registered"></i>
																  <p> AICTE LITE Program Registration </p>
																</a>
															</li>
																									</ul>
											</li>
																					<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=stud_att_STD" class="nav-link" title="Attendance">
												  <i class="nav-icon fas  fa-registered"></i>
												  <p> Attendance </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=Attendance_std" class="nav-link" title="PAT Attendance">
												  <i class="nav-icon fas fa-handshake"></i>
												  <p> PAT Attendance </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=std_att_register" class="nav-link" title="Attendance Register">
												  <i class="nav-icon fas fa-hand-point-left"></i>
												  <p> Attendance Register </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=proj_title_allotment" class="nav-link" title="Project Selection & Allotment">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Selection & Allotment </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=aat_qst_select_std" class="nav-link" title="AAT Question Selection">
												  <i class="nav-icon fas fa-plus"></i>
												  <p> AAT Question Selection </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=tm_allotment" class="nav-link" title="Project Team Member Selection">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Team Member Selection </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=prj_thesis_report_STD" class="nav-link" title="Project Work /Thesis Report">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Project Work /Thesis Report </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Requisitions">
								  <i class="nav-icon fas fa-graduation-cap"></i>
								  <p>Requisitions <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=req_certificate" class="nav-link" title="Certificate Request">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Certificate Request </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=req_trans_stud" class="nav-link" title="Transcript / Duplicate / Name Correction Memo">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Transcript / Duplicate / Name Correction Memo </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=skill_reg_frm" class="nav-link" title="Skill Program">
												  <i class="nav-icon fas fa-check-circle"></i>
												  <p> Skill Program </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Print Forms">
								  <i class="nav-icon fas fa-print"></i>
								  <p>Print Forms <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=print_no_due" class="nav-link" title="No Dues">
												  <i class="nav-icon fas fa-print"></i>
												  <p> No Dues </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=print_tc_due" class="nav-link" title="TC Form">
												  <i class="nav-icon fas fa-print"></i>
												  <p> TC Form </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=acc_register_std" class="nav-link " title="Accession Register">
								  <i class="nav-icon fas fa-hand-point-left"></i>
								  <p> Accession Register </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=workshop_Registration" class="nav-link " title="2023 MCUT-IARE ONLINE WORKSHOP">
								  <i class="nav-icon fas fa-registered"></i>
								  <p> 2023 MCUT- IARE ONLINE WORKSHOP Registration </p>
								</a>
							</li>
													<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Payments">
								  <i class="nav-icon fas fa-money-bill"></i>
								  <p>Payments <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment" class="nav-link" title="Online Fees Payment">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Online Fees Payment </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment_ccav" class="nav-link" title="Online Fees Payment CCAV">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Online Fees Payment CCAV </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=fee_payment_status" class="nav-link" title="Fee Status">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Fee Status </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=BC_STD" class="nav-link " title="Bonafide Certificate">
								  <i class="nav-icon fas fa-money-bill"></i>
								  <p> Bonafide Certificate </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=TT_std" class="nav-link " title="Timetable">
								  <i class="nav-icon fas fa-hand-point-left"></i>
								  <p> Timetable </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=mybox" class="nav-link " title="My Box">
								  <i class="nav-icon fas fa-inbox"></i>
								  <p> My Box </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=bus_registration" class="nav-link " title="">
								  <i class="nav-icon fas fa-registered"></i>
								  <p> Bus Registration </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=up_photo_std" class="nav-link " title="Upload Birth Certificate">
								  <i class="nav-icon fas fa-upload"></i>
								  <p> Upload Birth Certificate </p>
								</a>
							</li>
													<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=up_abc_std" class="nav-link " title="Update Academic Bank of credit">
								  <i class="nav-icon fas fa-edit"></i>
								  <p> Update Academic Bank of credit </p>
								</a>
							</li>
													<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Uploads">
								  <i class="nav-icon fas fa-upload"></i>
								  <p>Uploads <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=up_fp_std" class="nav-link" title="Upload Field Project">
												  <i class="nav-icon fas fa-money-bill"></i>
												  <p> Upload Field Project </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=upload_cvn_std" class="nav-link" title="Upload CVC Certificate">
												  <i class="nav-icon fas fa-certificate"></i>
												  <p> Upload CVC Certificate </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=aat_upload" class="nav-link" title="AAT (Tech Talk / Seminar Talk)">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> AAT (Tech Talk) </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=project_upload" class="nav-link" title="Upload Project Work">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> Upload Project Work </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=upload_aat_2" class="nav-link" title="AAT-II">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> AAT-II </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=labrecord_std" class="nav-link" title="Lab Record">
												  <i class="nav-icon fas fa-upload"></i>
												  <p> Lab Record </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item has-treeview">
								<a href="#" class="nav-link" title="Feedback">
								  <i class="nav-icon fas fa-comment"></i>
								  <p>Feedback <i class="fas fa-angle-left right"></i></p>
								</a>
								<ul class="nav nav-treeview">
																			<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=esf" class="nav-link" title="Early Semester Feedback">
												  <i class="nav-icon fas "></i>
												  <p> Early Semester Feedback </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=obe_fb_std" class="nav-link" title="OBE Feedback">
												  <i class="nav-icon fas "></i>
												  <p> OBE Feedback </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=std_review_syllabus" class="nav-link" title="Design and Review of Syllabus">
												  <i class="nav-icon fas "></i>
												  <p> Design and Review of Syllabus </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=ss_std" class="nav-link" title="Satisfaction Survey">
												  <i class="nav-icon fas "></i>
												  <p> Satisfaction Survey </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=placement_std" class="nav-link" title="Placement Experience">
												  <i class="nav-icon fas "></i>
												  <p> Placement Experience </p>
												</a>
											</li>
																				<li class="nav-item">
												<a href="https://samvidha.iare.ac.in/home?action=ns" class="nav-link" title="NAAC SURVEY">
												  <i class="nav-icon fas "></i>
												  <p> NAAC SURVEY </p>
												</a>
											</li>
																	</ul>
							</li>
														<li class="nav-item">
								<a href="https://samvidha.iare.ac.in/home?action=std_bio" class="nav-link " title="Biometric ">
								  <i class="nav-icon fas fa-fingerprint"></i>
								  <p> Biometric </p>
								</a>
							</li>
									</ul>
		</nav>
      <!-- /.sidebar-menu -->
    </div>
    <!-- /.sidebar -->
  </aside>
<style>
#myInput {
  background-image: url('/images/searchicon.png');
  background-position:10px 3px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 16px;
  padding:3px 20px 3px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}
</style>
<script>
  var parent = $("ul.sidebar-menu li.active").closest("ul").closest("li");
  if (parent[0] != undefined)
    $(parent[0]).addClass("active");

$(document).ready(function(){
  $("#myInput").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $(".nav-sidebar li").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});

</script><!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <section class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1>profile</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active">profile</li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
		<div class="container-fluid">
			<div class="row">
				<div class="col-md-6">
					<!-- Profile Image -->
					<div class="card card-primary card-outline">
						<div class="card-body box-profile">
							<div class="text-center">
																<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/22951A66F3.jpg" class="profile-user-img img-fluid img-circle" title="BOORLA SWATHI" alt="BOORLA SWATHI">
							</div>
							<h3 class="profile-username text-center">BOORLA SWATHI</h3>
														<p class="text-muted text-center">Computer Science and Engineering (AI & ML)</p>
						</div>
						<!-- /.card-body -->
					</div>
										<div class="card card-primary">
						<div class="card-header bg-teal btn" data-card-widget="collapse">
							<h3 class="card-title">General</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-4">Roll Number</dt>
								<dd class="col-sm-8">22951A66F3</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">ABC ID</dt>
								<dd class="col-sm-8">487-216-427-149</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">JNTUH AEBAS</dt>
								<dd class="col-sm-8">218129-237742</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Name</dt>
								<dd class="col-sm-8">BOORLA SWATHI</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">AAdhar Number</dt>
								<dd class="col-sm-8">2357 1415 2117</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Branch</dt>
								<dd class="col-sm-8">Computer Science and Engineering (AI & ML)</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Year/Sem</dt>
								<dd class="col-sm-8">II B.Tech II Sem</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Section</dt>
								<dd class="col-sm-8">C</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Gender</dt>
								<dd class="col-sm-8">F</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Name</dt>
								<dd class="col-sm-8">BOORLA SRINIVAS</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Mother Name</dt>
								<dd class="col-sm-8">BOORLA SURATHKALA</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Occupation Type</dt>
								<dd class="col-sm-8">Business</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Father Occupation</dt>
								<dd class="col-sm-8">BUISSINESS</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Date of Birth</dt>
								<dd class="col-sm-8">20-10-2004</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Date of Joining</dt>
								<dd class="col-sm-8">20-10-2022</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Regulation</dt>
								<dd class="col-sm-8">R20</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Status</dt>
								<dd class="col-sm-8">Studying</dd>
								
							</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-lightblue btn" data-card-widget="collapse">
							<h3 class="card-title ">Contacts</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<strong><i class="fas fa-lg fa-building mr-1"></i> Present Address</strong>
							<p class="text-muted">H.NO: 3-7-705/2/13, VIJETHA MUKUNDA TOWERS, BLOCK-A , FLAT NO: 303, VAVILALAPALLY, OPP GUNDU HANUMAN TEMPLE LANE</p>
							<hr>
							<strong><i class="fas fa-lg fa-building mr-1"></i> Permanent Address</strong>
							<p class="text-muted">H.NO: 3-7-705/2/13, VIJETHA MUKUNDA TOWERS, BLOCK-A , FLAT NO: 303, VAVILALAPALLY, OPP GUNDU HANUMAN TEMPLE LANE</p>
							<hr>
							<strong><i class="fas fa-phone mr-1"></i> Student Phone</strong>
							<p class="text-muted">8639805437</p>
							<hr>
							<strong><i class="fas fa-phone mr-1"></i> Parent Phone</strong>
							<p class="text-muted">9848533450</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Student Email-id</strong>
							<p class="text-muted">swathiboorla800@gmail.com</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Parent Email-id</strong>
							<p class="text-muted">Srinivas984883@gmail.com</p>
														<hr>
							<strong><i class="fas fa-envelope mr-1"></i> Domain Email-id</strong>
							<p class="text-muted">22951A66F3@iare.ac.in</p>
													</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="card card-primary">
						<div class="card-header bg-pink btn" data-card-widget="collapse">
							<h3 class="card-title ">Administrative Information</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<!-- /.card-header -->
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-4">Admission No</dt>
								<dd class="col-sm-8">7732</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">EAMCET RANK</dt>
								<dd class="col-sm-8">20</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Admission Type</dt>
								<dd class="col-sm-8">Management</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Tuition Fee</dt>
								<dd class="col-sm-8">101000</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Tuition Fee Waiver Amount</dt>
								<dd class="col-sm-8">0</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">PHC</dt>
								<dd class="col-sm-8">N</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Fee Category</dt>
								<dd class="col-sm-8">FEE-NOT-EXEMPTED</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Caste Category</dt>
								<dd class="col-sm-8">OC</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Region</dt>
								<dd class="col-sm-8">OU</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-4">Religion</dt>
								<dd class="col-sm-8">HINDU</dd>
							</dl>
						</div>
						<!-- /.card-body -->
					</div>
					<!-- /.card -->
					<div class="card card-primary">
						<div class="card-header bg-teal" data-card-widget="collapse">
							<h3 class="card-title ">Marks Details</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">
								<dt class="col-sm-8">SSC Percentage/CBSE</dt>
								<dd class="col-sm-4">10.00</dd>
								<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-8">Inter Percentage/Diploma</dt>
								<dd class="col-sm-4">74.30</dd>
																<div class="col-sm-12 dropdown-divider"></div>
								<dt class="col-sm-8">Degree Percentage</dt>
								<dd class="col-sm-4"></dd>
															</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-orange " data-card-widget="collapse">
							<h3 class="card-title ">Academic Progress</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body">
							<dl class="row">		
																<dt class="col-sm-4">I B.Tech</dt>
									<dd class="col-sm-8">Promoted to Next Semester</dd>
								 
									<div class="col-sm-12 dropdown-divider"></div>
																	<dt class="col-sm-4">II B.Tech I Sem</dt>
									<dd class="col-sm-8">Promoted to Next Semester</dd>
								 
									<div class="col-sm-12 dropdown-divider"></div>
																	<dt class="col-sm-4">II B.Tech II Sem</dt>
									<dd class="col-sm-8">Studying</dd>
															</dl>
						</div>
					</div>
					<div class="card card-primary">
						<div class="card-header bg-success">
							<h3 class="card-title ">Disciplinay Actions</h3>
						</div>
					</div>
					<div class="card card-lightblue" >
						<div class="card-header bg-lightblue" data-card-widget="collapse">
							<h3 class="card-title">Group Personal Accident Policy</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body p-0">
							<table class="table table-striped table-hover">
								<thead>
									<tr>
										<th style="width: 10px">S.no</th>
										<th>AY</th>
										<th>Status</th>
										<th>View</th>
									</tr>
								</thead>
																<tbody>
																				<tr>
												<td>1</td>
												<td>Group Personal Accident Policy - 2023-24</td>
												<td>Active</td>
												<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/Group_Policy/Student_2023-24.pdf' data-type="pdf" class="btn btn-sm bg-maroon display" target='_BLANK' alt="Group Personal Accident Policy" title="Group Personal Accident Policy"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></a></td>
											</tr>
																	</tbody>
							</table>
						</div>
					</div>
					<div class="card card-lightblue" >
						<div class="card-header bg-lightblue" data-card-widget="collapse">
							<h3 class="card-title">Certificates List</h3>
							<div class="card-tools">
								<button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i></button>
							</div>
						</div>
						<div class="card-body p-0">
							<table class="table table-striped table-hover">
								<thead>
									<tr>
										<th style="width: 10px">S.no</th>
										<th>Certificate</th>
										<th>View</th>
									</tr>
								</thead>
								<tbody>
																			<tr>
											<td>2</td>
											<td>SSC CERTIFICATE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/DOCS/22951A66F3_SSC.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>3</td>
											<td>INTER CERTIFICATE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/DOCS/22951A66F3_INTER.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>4</td>
											<td>Prev Institue TransferCerticate</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/DOCS/22951A66F3_TC.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>5</td>
											<td>INTER BONAFIDE</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/DOCS/22951A66F3_INTER_BONAFIDE.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																			<tr>
											<td>6</td>
											<td>SCHOOL BONAFIDE 2</td>
											<td><a href='https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66F3/DOCS/22951A66F3_SCHOOL_BC_2.jpg' data-type="jpg" class="btn btn-sm bg-maroon display" target='_BLANK' alt="View Certificate" title="View Certificate"><i class="fa fa-eye"></i> <i class="fa fa-certificate"></i></td>
										</tr>
																	</tbody>
							</table>
						</div>
					</div>
				</div>
				<div class="col-md-12">
										<div class="bg-success">
						<h4 class="text-center">Overall Conduct is GOOD</h4>
					</div>
				</div>
			</div>
        <!-- /.row -->
		</div><!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>
<div class="modal fade" id="modal-update_project">
	<div class="modal-dialog modal-xl">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close btn btn-danger" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">&times;</span>
				</button>
			</div>
			<div class="modal-body">
				<div class="col-sm-12 mgauto dataTables_wrapper">
					<img src="" id="img_doc" width="100%" height="600" style="border: none;"/>
					<iframe id="fram_doc" src="" width="100%" height="600" style="border: none;"></iframe>
				</div>
			</div>
			<div class="modal-footer justify-content-between">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Close</button>
			</div>
		</div>
		<!-- /.modal-content -->
	</div>
	<!-- /.modal-dialog -->
</div>
<script type="text/javascript">
	$(document).ready(function () {
		$(".display").click(function(e){
			e.preventDefault();
			if($(this).data("type") == 'pdf'){
				$('#fram_doc').attr('src',$(this).attr("href")+"#toolbar=0&amp;navpanes=0&amp;scrollbar=0");
				$('#fram_doc').show();
				$('#img_doc').hide();
			}else if($(this).data("type") == 'jpg'){
				$('#fram_doc').hide();
				$('#img_doc').attr('src',$(this).attr("href"));
				$('#img_doc').show();
			}
			$('#modal-update_project').modal({backdrop: 'static', keyboard: false},'show');
		});
	});
</script></div>
<footer class="main-footer">
  <strong>Copyright &copy; 2024  Institute of Aeronautical Engineering.</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All rights reserved.
</footer>
	
	


<!-- ChartJS -->
<script src="https://samvidha.iare.ac.in/plugins/chart.js/Chart.min.js"></script>

<!-- Sparkline -->
<script src="https://samvidha.iare.ac.in/plugins/sparklines/sparkline.js"></script>

<!-- jQuery Knob Chart -->
<script src="https://samvidha.iare.ac.in/plugins/jquery-knob/jquery.knob.min.js"></script>
<!-- daterangepicker -->
<script src="https://samvidha.iare.ac.in/plugins/moment/moment.min.js"></script>
<script src="https://samvidha.iare.ac.in/plugins/daterangepicker/daterangepicker.js"></script>
<!-- Bootstrap Switch -->
<script src="https://samvidha.iare.ac.in/plugins/bootstrap-switch/js/bootstrap-switch.min.js"></script>
<!-- Tempusdominus Bootstrap 4 -->
<script src="https://samvidha.iare.ac.in/plugins/tempusdominus-bootstrap-4/js/tempusdominus-bootstrap-4.min.js"></script>
<!-- Summernote -->
<script src="https://samvidha.iare.ac.in/plugins/summernote/summernote-bs4.min.js"></script>
<!-- overlayScrollbars -->
<script src="https://samvidha.iare.ac.in/plugins/overlayScrollbars/js/jquery.overlayScrollbars.min.js"></script>
<!-- AdminLTE App -->
<script src="https://samvidha.iare.ac.in/dist/js/adminlte.js"></script>

<!-- AdminLTE for demo purposes -->
<script src="https://samvidha.iare.ac.in/dist/js/demo.js"></script>
	<script>
	$(document).ready(function(){  
		function check_session(){
			$.ajax({
				url:"pages/layout/check_session.php",
				method:"POST",
				success:function(data)
				{
					if(data == '1')
					{
						//alert('Your session has been expired!');  
						window.location.href="index";
					}
				}
			})
		}
		setInterval(function(){
			check_session();
		}, 60000);  //60000 means 60 seconds
	});  
	$("html").on("contextmenu",function(e){
		return false;
    });
	$('#fram_doc').bind('contextmenu',function(e){ 
		return false; 
	});
	
	$(document).bind("menubar",function(e) {
		//e.preventDefault();
	});
	
	$(document).keydown(function(e){
		
		if(e.ctrlKey && e.keyCode == 83){
			e.preventDefault(); 
			return false;
		}
		if(e.which === 123 || e.which === 17 || e.which === 18 || e.which === 16){
		   e.preventDefault(); 
		   return false;
		}
		if ((e.ctrlKey && e.shiftKey && e.keyCode == 73) || (e.ctrlKey && e.keyCode==73) || (e.ctrlKey && e.shiftKey && e.keyCode == 74)  || (e.altKey && e.keyCode == 70)) {
			 e.preventDefault(); 
			return false;
		}
		//alert(e.keyCode);
	
	});
	
	
  $.widget.bridge('uibutton', $.ui.button)
</script></body>
</html>

"""


soup = BeautifulSoup(html_content_2,'html.parser')
data = {}

for dt in soup.find_all('dt'):
    key = dt.get_text(strip=True)
    dd = dt.find_next_sibling('dd')
    if dd:
        value = dd.get_text(strip=True)
        data[key] = value


for  strong in soup.find_all('strong'):
    key = strong.get_text(strip=True)
    p = strong.find_next_sibling('p')
    if p:
        value = p.get_text(strip=True)
        data[key] = value



sections = [
    ["Name", "Roll Number", "JNTUH AEBAS", "ABC ID"],
    ["Branch", "Year/Sem", "Section", "Admission No", "EAMCET RANK", "Date of Joining"],
    ["AAdhar Number", "Date of Birth"],
    ["Student Phone", "Student Email-id", "Domain Email-id"],
    ["Parent Phone", "Parent Email-id"]
]

profile_details_message = """
```Profile Details
"""


for section in sections:
    profile_details_message += "\n---\n"
    for key in section:
        value = data.get(key, "N/A")
        details_message = (f"\n {key}: {value} \n")
        profile_details_message += details_message 
        
profile_details_message += '\n---\n```'

print(profile_details_message)


        
        
