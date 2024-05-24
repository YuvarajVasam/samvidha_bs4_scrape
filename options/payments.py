from bs4 import BeautifulSoup 

html_content_paid = """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>IARE - Online Fees Payment - Student</title>
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

</script>						<div class="content-wrapper">
							<!-- Content Header (Page header) -->
							<section class="content-header">
								<div class="container-fluid">
									<div class="row mb-2">
										<div class="col-sm-6"><h1>Online Fees Payment</h1></div>
										<div class="col-sm-6">
											<ol class="breadcrumb float-sm-right">
											  <li class="breadcrumb-item"><a href="#">Home</a></li>
											  <li class="breadcrumb-item active">Online Fees Payment</li>
											</ol>
										</div>
									</div>
								</div><!-- /.container-fluid -->
							</section>
							<!-- Main content -->
							<section class="content">
									<div class="card card-info">
		<div class="card-header">
			<!--<h3 class="card-title">Fee Payment for the Academic Year - </h3>-->
		</div>
		<div class="card-body table-responsive p-0">
			
			<table class="table table-striped table-sm table-bordered table-hover ">
				<thead>
					<tr>
						<th style="width: 10px">#</th>
						<th>Fee Type</th>
						<th>Track Id</th>
						<!--<th>Payment Mode</th>-->
						<th>Payment Date</th>
						<th>Amount</th>
						<th>Pay/Print</th>
					</tr>
					<tr>
						<td>1</td>
						<td>Tution Fee (22951A66F3)</td>
						<td>tfBCAT2024-25_22951A66F3</td>
						<!--<td></td>-->
						<td>02 Apr, 2024</td>
													<td>101000</td>
							<td>
								<input type="hidden" id='tf_trackid' value="tfBCAT2024-25_22951A66F3">
								<input type="hidden" id='tf_paid_amount_words' value="one lakh one thousand ">
								<input type="hidden" id='tf_paid_amount' value="101000">
								<input type="hidden" id='tf_payment_date' value="02 Apr, 2024">
								<input type="hidden" id='tf_ay' value="2024-25">
								<input type="hidden" id='tf_confirm' value="1">
								<input type="button" id="tf_print" name='tf' class="btn btn-success Receipt" value="Print Receipt">
							</td>
											</tr>
																<tr>
							<td>2</td>
							<td>Bus Fee <br>RouteNo: <br> Stop Name: </td>
							<td></td>
							<!--<td></td>-->
							<td></td>
							<td>NO</td>
							<td>
																	<a href='home?action=bus_registration' class="btn btn-success btn-sm">Register For Transport</a>
															</td>
						</tr>
										<!--<tr><td></td><td>Hostel Fee</td><td></td><td></td><td></td><td></td><td></td></tr>
					<tr><td></td><td>Regular Examination Fee</td><td><td></td><td></td><td></td></td><td></td></tr>
					<tr><td></td><td>Supplementary Examination Fee</td><td></td><td></td><td></td><td></td><td></td></tr>-->
				</thead>
				<tbody>
					
				</tbody>
			</table>
			<br/><br/><br/>
		</div>
	</div>
<div class="modal fade" id="modal-print_receipt">
	<div class="modal-dialog modal-lg">
		<div class="modal-content">
			<div class="modal-header">
				<h4 class="modal-title">Print Fee Receipt</h4>
			</div>
			<div class="modal-body" id="printdiv">
				<table style="margin:20px auto; padding-left:20px;border: solid 0px #7198FD; !important; width:700px;font-size:18px">
					<td colspan="2" style="text-align:center"><img src="https://samvidha.iare.ac.in/images/logo_new.jpg" height="95px"><br/><br/></td>
					<tr><td colspan="2" style="text-align: center; font-weight:bold; font-size:20px"> <span id='recfor'></span> RECEIPT<br><br></td></tr>
					<tr><td style="text-align:left" colspan=1>TrackID: <b id="trackid"></b></td><td style="text-align:right" colspan=1>Date: <b id="pdate"> </b><br></td></tr> 
										<tr><td colspan="2"><br><p style="text-align:justify;line-height:26px">Received an amount of Rs. <span id="amount"></span> (Inwords: Rupees <span id="amountwords"></span> only) towards <span id="fheader"></span> for the academic year <span id="ay"></span> from Ms. BOORLA SWATHI, bearing Roll No. 22951A66F3,
studying III B.Tech (Computer Science and Engineering (AI & ML)) in this Institution.<br/><br/>
					<span id="bus"></span>
										The next payment date for the academic year 2025-26 falls due on 30 April, 2025.
					</p></td></tr>
										<tr><td></td><td colspan="2" style="font-weight:bold; text-align:right"><br><br>PRINCIPAL</td></tr>
				</table>
			</div>
			<div class="modal-footer justify-content-between">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
				<button type="submit" id='btnPrint' name='btnPrint' class="btn btn-primary">Print</button>
			</div>
			
		</div>
		<!-- /.modal-content -->
	</div>
	<!-- /.modal-dialog -->
</div>
<script>
	$("#btnPrint").click(function () {
		var cloned = $('#printdiv').clone();
		var printSection = $('#printSection');
		if (printSection.length == 0) {
			printSection = $('<div id="printSection"></div>')
			$('body').append(printSection);
		}
		printSection.append(cloned);
		var toggleBody = $('body *:visible');
		toggleBody.hide();
		$('#printSection, #printSection *').show();
		window.print();
		printSection.remove();
		toggleBody.show();
	});
	$(".Receipt").click(function(event){
		event.preventDefault(); //prevent default action 
		var id= $(this).attr("id");
		var rprint = 0;
		if(id=='tf_print'){
			if($('#tf_confirm').val() == 1) rprint = 1;
		}
		if(id=='bf_print'){
			if($('#bf_confirm').val()) rprint = 1;
		}
		if(id=='mf'){
			if($('#mf_confirm').val()) rprint = 1;
		}
		if(rprint == 0){
			Swal.fire({
				title: 'Receipt will be available with in 48hr of payment, after verification.',
				text: 'In case of any query please contact V. Mahidhar Reddy (Contact no. 86393 13083)'
				//showCancelButton: true,
			});
			return false;
		}else{
			var type = id.replace("_print", "");
			if(id=='mf'){
				$('#fheader').html('JNTUH/NBA Fee');
				$("#recfor").html("JNTUH/NBA FEE");
			}else if(id=='tf_print'){
				if(1 == 4){
					$('#fheader').html('Ph.D Course Work Fee');
					$("#recfor").html('Ph.D COURSE WORK FEE');
				}else{
					$('#fheader').html('Tuition Fee');
					$("#recfor").html('TUITION FEE');
				}
			}else if(id=='bf_print'){
				$('#fheader').html('Bus Fee');
				$("#recfor").html('BUS FEE');
				//$('#bus').html();
			}else{
				if(1 == 4){
					$('#fheader').html('Ph.D Course Work Fee');
					$("#recfor").html('Ph.D COURSE WORK FEE');
				}else{
					$('#fheader').html('Tuition Fee');
					$("#recfor").html('TUITION FEE');
				}
			}
			$('#trackid').html($('#'+type+'_trackid').val());
			$('#pdate').html($('#'+type+'_payment_date').val());
			$('#amount').html($('#'+type+'_paid_amount').val());
			$('#ay').html($('#'+type+'_ay').val());
			$('#trackid').html($('#'+type+'_trackid').val());
			$('#amountwords').html($('#'+type+'_paid_amount_words').val());
			$('#modal-print_receipt').modal();
		}
	})
</script>							</section class="content">
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

html_content_notpaid= """

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<title>IARE - Online Fees Payment - Student</title>
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
										<div class="col-sm-6"><h1>Online Fees Payment</h1></div>
										<div class="col-sm-6">
											<ol class="breadcrumb float-sm-right">
											  <li class="breadcrumb-item"><a href="#">Home</a></li>
											  <li class="breadcrumb-item active">Online Fees Payment</li>
											</ol>
										</div>
									</div>
								</div><!-- /.container-fluid -->
							</section>
							<!-- Main content -->
							<section class="content">
									<div class="card card-info">
		<div class="card-header">
			<!--<h3 class="card-title">Fee Payment for the Academic Year - </h3>-->
		</div>
		<div class="card-body table-responsive p-0">
			
			<table class="table table-striped table-sm table-bordered table-hover ">
				<thead>
					<tr>
						<th style="width: 10px">#</th>
						<th>Fee Type</th>
						<th>Track Id</th>
						<!--<th>Payment Mode</th>-->
						<th>Payment Date</th>
						<th>Amount</th>
						<th>Pay/Print</th>
					</tr>
					<tr>
						<td>1</td>
						<td>Tution Fee (22951A66J6)</td>
						<td></td>
						<!--<td></td>-->
						<td>extra days: 0</td>
													<td>66000</td>
							<td><a style="" href="https://www.eduqfix.com/checkout/integration/payment?merchantId=PERP00002&command=INITIATE&schemeCode=PERP00002_S7&payload=FoW4Ll_XISFXczXHQbz6OexOU3y19p2_lJDLdCbhzjalyrPw9XiSR4mwZpzRhFL1BF4JwYPMjGfPs3ahK2Ha0YE5W1dr_lEfwIgoKsJHa-AKX82ZheqiAMjfyVe3I9uClCYedl-t_IrlN004Rxk1UQ-cjdlA6OfDUWdiFutK6sqM0vGHAcXiwbxx_4XpwOJQGXahXBK2mOyCjqxemKp5oqxrxcztEOup0yniKIe4hSdBY_fqoN-uYpL_FObqNtg3fDc_qtsWfnsPoMNMT6-D3sOiuYcBIPcNM2g6tPaLy1RAOqGVLyPGJkfMEFVl6c7AH3GmGV_t1d_fQqx3yQZdEOc1Tlux9F27MBCNJIKDzvB2mD-9Yag_8du-rpdsE0DJHpwFYB8B4KGCv2ADkX-fCmWsaLxE020juYu3v28dIU9ASb9vRKa3P4DhqOxjGcC9UfGvSbjkH1o7KEf35f72rjelyaaEG3QhuXYzCRRhP3QBInOPtzh_uF6ZyqgwEaNdJuGOumQolyZldiTHx5TxzAdtH4Y-hT9tIwMe4v3LJ7s" class="btn btn-sm bg-gradient-info"><i class="far fa-credit-card"></i> Pay Now</a></td>
											</tr>
																<tr>
							<td>2</td>
							<td>Bus Fee <br>RouteNo: <br> Stop Name: </td>
							<td></td>
							<!--<td></td>-->
							<td></td>
							<td>NO</td>
							<td>
																	<a href='home?action=bus_registration' class="btn btn-success btn-sm">Register For Transport</a>
															</td>
						</tr>
										<!--<tr><td></td><td>Hostel Fee</td><td></td><td></td><td></td><td></td><td></td></tr>
					<tr><td></td><td>Regular Examination Fee</td><td><td></td><td></td><td></td></td><td></td></tr>
					<tr><td></td><td>Supplementary Examination Fee</td><td></td><td></td><td></td><td></td><td></td></tr>-->
				</thead>
				<tbody>
					
				</tbody>
			</table>
			<br/><br/><br/>
		</div>
	</div>
<div class="modal fade" id="modal-print_receipt">
	<div class="modal-dialog modal-lg">
		<div class="modal-content">
			<div class="modal-header">
				<h4 class="modal-title">Print Fee Receipt</h4>
			</div>
			<div class="modal-body" id="printdiv">
				<table style="margin:20px auto; padding-left:20px;border: solid 0px #7198FD; !important; width:700px;font-size:18px">
					<td colspan="2" style="text-align:center"><img src="https://samvidha.iare.ac.in/images/logo_new.jpg" height="95px"><br/><br/></td>
					<tr><td colspan="2" style="text-align: center; font-weight:bold; font-size:20px"> <span id='recfor'></span> RECEIPT<br><br></td></tr>
					<tr><td style="text-align:left" colspan=1>TrackID: <b id="trackid"></b></td><td style="text-align:right" colspan=1>Date: <b id="pdate"> </b><br></td></tr> 
										<tr><td colspan="2"><br><p style="text-align:justify;line-height:26px">Received an amount of Rs. <span id="amount"></span> (Inwords: Rupees <span id="amountwords"></span> only) towards <span id="fheader"></span> for the academic year <span id="ay"></span> from Mr. VASAM YUVARAJ, bearing Roll No. 22951A66J6,
studying III B.Tech (Computer Science and Engineering (AI & ML)) in this Institution.<br/><br/>
					<span id="bus"></span>
										The next payment date for the academic year 2025-26 falls due on 30 April, 2025.
					</p></td></tr>
										<tr><td></td><td colspan="2" style="font-weight:bold; text-align:right"><br><br>PRINCIPAL</td></tr>
				</table>
			</div>
			<div class="modal-footer justify-content-between">
				<button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
				<button type="submit" id='btnPrint' name='btnPrint' class="btn btn-primary">Print</button>
			</div>
			
		</div>
		<!-- /.modal-content -->
	</div>
	<!-- /.modal-dialog -->
</div>
<script>
	$("#btnPrint").click(function () {
		var cloned = $('#printdiv').clone();
		var printSection = $('#printSection');
		if (printSection.length == 0) {
			printSection = $('<div id="printSection"></div>')
			$('body').append(printSection);
		}
		printSection.append(cloned);
		var toggleBody = $('body *:visible');
		toggleBody.hide();
		$('#printSection, #printSection *').show();
		window.print();
		printSection.remove();
		toggleBody.show();
	});
	$(".Receipt").click(function(event){
		event.preventDefault(); //prevent default action 
		var id= $(this).attr("id");
		var rprint = 0;
		if(id=='tf_print'){
			if($('#tf_confirm').val() == 1) rprint = 1;
		}
		if(id=='bf_print'){
			if($('#bf_confirm').val()) rprint = 1;
		}
		if(id=='mf'){
			if($('#mf_confirm').val()) rprint = 1;
		}
		if(rprint == 0){
			Swal.fire({
				title: 'Receipt will be available with in 48hr of payment, after verification.',
				text: 'In case of any query please contact V. Mahidhar Reddy (Contact no. 86393 13083)'
				//showCancelButton: true,
			});
			return false;
		}else{
			var type = id.replace("_print", "");
			if(id=='mf'){
				$('#fheader').html('JNTUH/NBA Fee');
				$("#recfor").html("JNTUH/NBA FEE");
			}else if(id=='tf_print'){
				if(1 == 4){
					$('#fheader').html('Ph.D Course Work Fee');
					$("#recfor").html('Ph.D COURSE WORK FEE');
				}else{
					$('#fheader').html('Tuition Fee');
					$("#recfor").html('TUITION FEE');
				}
			}else if(id=='bf_print'){
				$('#fheader').html('Bus Fee');
				$("#recfor").html('BUS FEE');
				//$('#bus').html();
			}else{
				if(1 == 4){
					$('#fheader').html('Ph.D Course Work Fee');
					$("#recfor").html('Ph.D COURSE WORK FEE');
				}else{
					$('#fheader').html('Tuition Fee');
					$("#recfor").html('TUITION FEE');
				}
			}
			$('#trackid').html($('#'+type+'_trackid').val());
			$('#pdate').html($('#'+type+'_payment_date').val());
			$('#amount').html($('#'+type+'_paid_amount').val());
			$('#ay').html($('#'+type+'_ay').val());
			$('#trackid').html($('#'+type+'_trackid').val());
			$('#amountwords').html($('#'+type+'_paid_amount_words').val());
			$('#modal-print_receipt').modal();
		}
	})
</script>							</section class="content">
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

soup = BeautifulSoup(html_content_notpaid,'html.parser')

rows = soup.table.thead.find_all('tr')
fee_row = rows[1].find_all('td')


rollno = fee_row[1].text[12:-1]
track_id = fee_row[2].text
payment_date = fee_row[3].text
amount = fee_row[4].text
status = "Not Paid"

if track_id != "":
    status = "Paid"

if status == "Paid":
    payment_message = f"""
```Tution Fee
RollNo: {rollno}
Amount: {amount}
Status: Paid 
Payment Date: {payment_date}
Track ID: {track_id}
```
"""
    print(payment_message)

else:
    payment_link = fee_row[5].a['href']
    payment_message = f"""
```Tution Fee
RollNo: {rollno}
Amount : {amount}
Status: Not Paid

Pay As Soon As Possible 
To Avoid Penalty...
```
"""
    print(payment_message)
    print(payment_link)





