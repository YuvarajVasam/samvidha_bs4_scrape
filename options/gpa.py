import re

text = """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>IARE - Credit Register - Student</title>
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

</script>						<div class="content-wrapper">
							<!-- Content Header (Page header) -->
							<section class="content-header">
								<div class="container-fluid">
									<div class="row mb-2">
										<div class="col-sm-6"><h1>Credit Register</h1></div>
										<div class="col-sm-6">
											<ol class="breadcrumb float-sm-right">
											  <li class="breadcrumb-item"><a href="#">Home</a></li>
											  <li class="breadcrumb-item active">Credit Register</li>
											</ol>
										</div>
									</div>
								</div><!-- /.container-fluid -->
							</section>
							<!-- Main content -->
							<section class="content">
									<style>
		.watermark {
			position: absolute;
			color: lightgray;
			opacity: 0.25;
			width: 100%;
			font-size:100px;
			font-size: 50px;
			margin-top: 100px;
			-webkit-transform:rotate(300deg);   
			text-align: center;
			z-index: 0;
		}
		.sem2{ margin-top: 400px;}
		.sem3{ margin-top: 700px;}
		.sem4{ margin-top: 1000px;}
		.sem5{ margin-top: 1300px;}
		.sem6{ margin-top: 1600px;}
		.sem7{ margin-top: 1900px;}
		.sem8{ margin-top: 2200px;}
	</style>
	<div class="card card-primary">
		<div class="card-body">
					
				<table align="center" width="900" class="table-bordered">
					<tr height=20>
						<td colspan='8' style='background: #7d7dfb;border:none;'></td>
						<td colspan="1" align="center" style='background: #7d7dfb;border:none;'></td>
						<td colspan='1' style='background: #7d7dfb;border:none;'> 
												<a href='home?action=credit_register&history=yes' style="color:#fff;background: #7d7dfb;" >
													<span style="float:right;padding-left:10px;margin-right:10px;font-size:12px;"><i class="fas fa-hand-point-right" aria-hidden="true"></i> <b>CREDIT REGISTER HISTORY</b></span>
						</a>
						</td>
					</tr>
					<tr class="text-center bg-olive disabled"><th colspan="11"> CREDIT REGISTER </th></tr>
					<tr>
						<td colspan="1" rowspan=4 style="padding:5px 0px" align='center' width="15%">
							<img src="https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/22951A66J6/22951A66J6.jpg" height='90' width='100' style="border: solid 5px #AAAAAA">
						</td>
					</tr>
					<tr height=20>
						<td colspan="2" style="text-align:left;">&nbsp;Roll Number  </td>
						<td colspan="8" style="text-align:left;">&nbsp;&nbsp;<b>22951A66J6</b>	</td> 
					</tr>
					<tr height=20>
						<td colspan="2" style="text-align:left;">&nbsp;Name</td>
						<td colspan="8" style="text-align:left;"><b>&nbsp;&nbsp;VASAM YUVARAJ</b>	</td>
					</tr>
					<tr height=20>
						<td colspan="2" style="text-align:left;">&nbsp;Branch</td>
						<td colspan="8" style="text-align:left;"><b>&nbsp;&nbsp;<b>Computer Science And Engineering (ai & Ml)</td>
					</tr>
				</table>
				
				<table align="center" width="900" class="table-bordered">
					<tr height="20" class="text-center bg-pink">
						<th style="width:40px;"> S.No </th>
						<th style="width:80px;"> Course Code </th>
						<th align="left" style="width:280px;"> Course Name </th>
						<th style="width:50px;"> Grade </th>
						<th style="width:80px;">Grade&nbsp;Point</th>
						<th style="width:50px;"> Status</th>
						<th style="width:50px;"> Credits </th>
						<th style="width:50px;"> Attendence % </th>
					</tr>
											<div class="watermark sem1">22951A66J6</div>
						<tr class="text-center bg-lightblue disabled">
							<th colspan="9" >I SEMESTER</th>
						</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>1</td>
									<td style='width:80px;'>AHSC02</td>
									<td style='width:280px;text-align:left;'>LINEAR ALGEBRA AND CALCULUS </td>
																		<td style='width:50px;'>A</td>
									<td style='width:80px;text-align:center;'>8</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>4.00</td>
									<td style='width:50px;'>88.64</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>2</td>
									<td style='width:80px;'>AHSC06</td>
									<td style='width:280px;text-align:left;'>CHEMISTRY</td>
																		<td style='width:50px;'>A</td>
									<td style='width:80px;text-align:center;'>8</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>2.00</td>
									<td style='width:50px;'>89.89</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>3</td>
									<td style='width:80px;'>AEEC01</td>
									<td style='width:280px;text-align:left;'>BASIC ELECTRICAL ENGINEERING</td>
																		<td style='width:50px;'>B+</td>
									<td style='width:80px;text-align:center;'>7</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>3.00</td>
									<td style='width:50px;'>100.00</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>4</td>
									<td style='width:80px;'>ACSC01</td>
									<td style='width:280px;text-align:left;'>PYTHON PROGRAMMING</td>
																		<td style='width:50px;'>B+</td>
									<td style='width:80px;text-align:center;'>7</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>3.00</td>
									<td style='width:50px;'>91.11</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>5</td>
									<td style='width:80px;'>ACSC06</td>
									<td style='width:280px;text-align:left;'>EXPERIENTIAL ENGINEERING EDUCATION (EXEED)- ACADEMIC SUCCESS</td>
																		<td style='width:50px;'>A+</td>
									<td style='width:80px;text-align:center;'>9</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.00</td>
									<td style='width:50px;'>86.96</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>6</td>
									<td style='width:80px;'>AEEC04</td>
									<td style='width:280px;text-align:left;'>BASIC ELECTRICAL ENGINEERING LABORATORY</td>
																		<td style='width:50px;'>S</td>
									<td style='width:80px;text-align:center;'>10</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.50</td>
									<td style='width:50px;'>83.33</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>7</td>
									<td style='width:80px;'>ACSC02</td>
									<td style='width:280px;text-align:left;'>PYTHON PROGRAMMING LABORATORY</td>
																		<td style='width:50px;'>A</td>
									<td style='width:80px;text-align:center;'>8</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.50</td>
									<td style='width:50px;'>84.62</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>8</td>
									<td style='width:80px;'>AMEC04</td>
									<td style='width:280px;text-align:left;'>ENGINEERING WORKSHOP PRACTICE</td>
																		<td style='width:50px;'>S</td>
									<td style='width:80px;text-align:center;'>10</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.00</td>
									<td style='width:50px;'>81.25</td>
								</tr>
												<tr class="text-center">
							<td colspan=3 class="text-right"> <strong>Total</strong> </td>
							<td>-</td>
							<td>-</td>
							<td></td>
							<td><strong>17</strong></td>
							<td>-</td>
						</tr>
						<tr class="bg-danger">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Semester Grade Point Average (SGPA) : 8 </td>
						</tr>
						<tr class="bg-teal">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Cumulative Grade Point Average (CGPA) : 8 </td>
						</tr>
											<div class="watermark sem2">22951A66J6</div>
						<tr class="text-center bg-lightblue disabled">
							<th colspan="9" >II SEMESTER</th>
						</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>1</td>
									<td style='width:80px;'>AHSC01</td>
									<td style='width:280px;text-align:left;'>ENGLISH</td>
																		<td style='width:50px;'>A</td>
									<td style='width:80px;text-align:center;'>8</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>3.00</td>
									<td style='width:50px;'>83.78</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>2</td>
									<td style='width:80px;'>AHSC08</td>
									<td style='width:280px;text-align:left;'>PROBABILITY AND STATISTICS</td>
																		<td style='width:50px;'>A+</td>
									<td style='width:80px;text-align:center;'>9</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>4.00</td>
									<td style='width:50px;'>86.17</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>3</td>
									<td style='width:80px;'>AHSC09</td>
									<td style='width:280px;text-align:left;'>APPLIED PHYSICS</td>
																		<td style='width:50px;'>A</td>
									<td style='width:80px;text-align:center;'>8</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>3.00</td>
									<td style='width:50px;'>82.72</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>4</td>
									<td style='width:80px;'>ACSC04</td>
									<td style='width:280px;text-align:left;'>PROGRAMMING FOR PROBLEM SOLVING USING C</td>
																		<td style='width:50px;'>A+</td>
									<td style='width:80px;text-align:center;'>9</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>3.00</td>
									<td style='width:50px;'>84.62</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>5</td>
									<td style='width:80px;'>AHSC04</td>
									<td style='width:280px;text-align:left;'>ENGLISH LANGUAGE AND COMMUNICATION SKILLS LABORATORY</td>
																		<td style='width:50px;'>A+</td>
									<td style='width:80px;text-align:center;'>9</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.00</td>
									<td style='width:50px;'>95.56</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>6</td>
									<td style='width:80px;'>AHSC05</td>
									<td style='width:280px;text-align:left;'>PHYSICS LABORATORY</td>
																		<td style='width:50px;'>A+</td>
									<td style='width:80px;text-align:center;'>9</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.50</td>
									<td style='width:50px;'>90.91</td>
								</tr>
														<tr align=center bgcolor="">
																	<td style='width:40px;'>7</td>
									<td style='width:80px;'>ACSC05</td>
									<td style='width:280px;text-align:left;'>PROGRAMMING FOR PROBLEM SOLVING USING C LABORATORY</td>
																		<td style='width:50px;'>S</td>
									<td style='width:80px;text-align:center;'>10</td>
									<td style='width:50px;'>P</td>
																		<td style='width:50px;'>1.50</td>
									<td style='width:50px;'>87.32</td>
								</tr>
												<tr class="text-center">
							<td colspan=3 class="text-right"> <strong>Total</strong> </td>
							<td>-</td>
							<td>-</td>
							<td></td>
							<td><strong>17</strong></td>
							<td>-</td>
						</tr>
						<tr class="bg-danger">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Semester Grade Point Average (SGPA) : 8.74 </td>
						</tr>
						<tr class="bg-teal">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Cumulative Grade Point Average (CGPA) : 8.37 </td>
						</tr>
											<div class="watermark sem3">22951A66J6</div>
						<tr class="text-center bg-lightblue disabled">
							<th colspan="9" >III SEMESTER</th>
						</tr>
													<tr align="center" >
								<td style='width:40px;'>1</td>
								<td style='width:80px;'>ACSC07</td>
								<td style='width:280px;text-align:left;'>COMPUTER ORGANIZATION AND ARCHITECTURE</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>2</td>
								<td style='width:80px;'>ACSC08</td>
								<td style='width:280px;text-align:left;'>DATA STRUCTURES</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>3</td>
								<td style='width:80px;'>ACSC12</td>
								<td style='width:280px;text-align:left;'>OPERATING SYSTEMS</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>4</td>
								<td style='width:80px;'>ACAC01</td>
								<td style='width:280px;text-align:left;'>PROBABILISTIC MODELING AND REASONING</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>4.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>5</td>
								<td style='width:80px;'>AECC08</td>
								<td style='width:280px;text-align:left;'>ANALOG AND DIGITAL ELECTRONICS</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>6</td>
								<td style='width:80px;'>ACSC09</td>
								<td style='width:280px;text-align:left;'>EXPERIENTIAL ENGINEERING EDUCATION (EXEED) - PROTOTYPE / DESIGN BUILDING</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>7</td>
								<td style='width:80px;'>ACSC10</td>
								<td style='width:280px;text-align:left;'>DATA STRUCTURES LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.50</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>8</td>
								<td style='width:80px;'>AITC03</td>
								<td style='width:280px;text-align:left;'>PROGRAMMING WITH OBJECTS LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.50</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>9</td>
								<td style='width:80px;'>ACSC11</td>
								<td style='width:280px;text-align:left;'>ADVANCED PYTHON PROGRAMMING LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>2.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>10</td>
								<td style='width:80px;'>AHSC10</td>
								<td style='width:280px;text-align:left;'>ESSENCE OF INDIAN TRADITIONAL KNOWLEDGE</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>0.00</td>
								<td class="text-center"></td>
							</tr>
												<tr class="text-center">
							<td colspan=3 class="text-right"> <strong>Total</strong> </td>
							<td>-</td>
							<td>-</td>
							<td></td>
							<td><strong>0</strong></td>
							<td>-</td>
						</tr>
						<tr class="bg-danger">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Semester Grade Point Average (SGPA) : - </td>
						</tr>
						<tr class="bg-teal">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Cumulative Grade Point Average (CGPA) : 8.37 </td>
						</tr>
											<div class="watermark sem4">22951A66J6</div>
						<tr class="text-center bg-lightblue disabled">
							<th colspan="9" >IV SEMESTER </th>
						</tr>
													<tr align="center" >
								<td style='width:40px;'>1</td>
								<td style='width:80px;'>AITC04</td>
								<td style='width:280px;text-align:left;'>THEORY OF COMPUTATION</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>4.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>2</td>
								<td style='width:80px;'>ACSC13</td>
								<td style='width:280px;text-align:left;'>DESIGN AND ANALYSIS OF ALGORITHMS</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>3</td>
								<td style='width:80px;'>AITC05</td>
								<td style='width:280px;text-align:left;'>DATABASE MANAGEMENT SYSTEMS</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>4</td>
								<td style='width:80px;'>AITC09</td>
								<td style='width:280px;text-align:left;'>WEB APPLICATION DEVELOPMENT</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>5</td>
								<td style='width:80px;'>ACAC03</td>
								<td style='width:280px;text-align:left;'>FOUNDATIONS OF MACHINE LEARNING</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>6</td>
								<td style='width:80px;'>AHSC15</td>
								<td style='width:280px;text-align:left;'>SOFT SKILLS AND INTERPERSONAL COMMUNICATION</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>3.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>7</td>
								<td style='width:80px;'>ACSC14</td>
								<td style='width:280px;text-align:left;'>EXPERIENTIAL ENGINEERING EDUCATION (EXEED) - FABRICATION / MODEL DEVELOPMENT</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>8</td>
								<td style='width:80px;'>AITC07</td>
								<td style='width:280px;text-align:left;'>DATABASE MANAGEMENT SYSTEMS LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.50</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>9</td>
								<td style='width:80px;'>AITC10</td>
								<td style='width:280px;text-align:left;'>WEB APPLICATION DEVELOPMENT LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>1.50</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>10</td>
								<td style='width:80px;'>ACAC04</td>
								<td style='width:280px;text-align:left;'>FOUNDATIONS OF MACHINE LEARNING LABORATORY</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>2.00</td>
								<td class="text-center">-</td>
							</tr>
													<tr align="center" >
								<td style='width:40px;'>11</td>
								<td style='width:80px;'>AHSC14</td>
								<td style='width:280px;text-align:left;'>INDIAN CONSTITUTION</td>
								<td colspan="3" class="text-center text-red">Not Registered for examination</td>
								<td style='width:50px;'>0.00</td>
								<td class="text-center"></td>
							</tr>
												<tr class="text-center">
							<td colspan=3 class="text-right"> <strong>Total</strong> </td>
							<td>-</td>
							<td>-</td>
							<td></td>
							<td><strong>0</strong></td>
							<td>-</td>
						</tr>
						<tr class="bg-danger">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Semester Grade Point Average (SGPA) : - </td>
						</tr>
						<tr class="bg-teal">
							<td colspan="9"  style='text-align:right;padding-right:10px;'>Cumulative Grade Point Average (CGPA) : 8.37 </td>
						</tr>
									</table>
								<div style="clear: both;background:#ffffff;">&nbsp;</div>
				<table align="center" class="table table-sm table-bordered" style="margin-top:5px;width: 900px;">
					<tr class="text-center bg-lightblue disabled">
						<th colspan='4'>Courses Due/Pending for Completion</th>
					</tr>
					<tr height="25" class="text-center bg-pink">
						<th width="60px">Course Category</th>
						<th width="80px">Required Course Count</th>
						<th width="60px">Registered Course Count</th>
						<th width="60px">Yet To Be Registered</th>
					</tr>
											<tr class="text-center">
							<td class="text-left" >FOUNDATION</td>
							<td>20</td>
							<td>17</td>
							<td class="text-danger">3</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >CORE</td>
							<td>30</td>
							<td>16</td>
							<td class="text-danger">14</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >PROFESSIONAL ELECTIVE</td>
							<td>6</td>
							<td></td>
							<td class="text-danger">6</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >OPEN ELECTIVE</td>
							<td>3</td>
							<td>1</td>
							<td class="text-danger">2</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >PROJECT WORK</td>
							<td>2</td>
							<td></td>
							<td class="text-danger">2</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >AUDIT</td>
							<td>2</td>
							<td>2</td>
							<td class="text-success">0</td>
						</tr>
												<tr class="text-center">
							<td class="text-left" >VALUE ADDED</td>
							<td>2</td>
							<td></td>
							<td class="text-danger">2</td>
						</tr>
											
				</table>
				<br/>
								<table align="center" width="900" class="table-bordered" style="margin-top:10px;" >
				<tr class="text-center bg-lightblue disabled">
					<th colspan="11">Letter Grades and Grade Point</th>
				</tr>
				<tr class="text-center bg-pink">
					<td>Range of Marks</td>
					<td>100 - 90</td>
					<td>89 - 80</td>
					<td>79 - 70</td>
					<td>69 - 60</td>
					<td>59 - 50</td>
					<td>49 - 40</td>
					<td>Below 40</td> 
					<td>Absent</td>
					<td style="width:80px;">Shortage of Attendence</td>
					<td style="width:100px;">Authorized Break of Study</td>
				</tr>
				<tr class="text-center">
					<td>Grade Point</td>
					<td>10</td>
					<td>9</td>
					<td>8</td>
					<td>7</td>
					<td>6</td>
					<td>5</td>
					<td>0</td>
					<td>0</td>
					<td>0</td>
					<td>0</td>
				</tr>
				<tr class="text-center">
					<td>Letter Grade</td>
					<td>S<br>(Superior)</td>
					<td>A+<br>(Excellent)</td>
					<td>A<br>(Very Good)</td>
					<td>B+<br>(Good) </td>
					<td>B<br>(Average)</td>
					<td>C<br>(Pass)</td>
					<td>F<br>(Fail)</td>
					<td>AB</td>
					<td>SA</td>
					<td>ABS</td>
				</tr>
				</table>
					</div>
	</div>
	

							</section class="content">
						</div>
						</div>
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

pattern = r'Semester Grade Point Average \(SGPA\) : (\d(?:\.\d\d)?)'

sgpa_values = re.findall(pattern,text)
sgpa_values = [float(x) for x in sgpa_values]
cgpa = round(sum(sgpa_values) / len(sgpa_values) , 2)

gpa_message = """
```GPA
⫸ SGPA 

"""

for i,sgpa in enumerate(sgpa_values,start = 1):
    # print(i,sgpa)
    sgpa_message = f'Semester-{i} : {sgpa} \n \n'
    gpa_message += sgpa_message 
    


gpa_message += f"""⫸ CGPA : {cgpa}  
```
"""

print(gpa_message)

