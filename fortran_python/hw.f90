double precision function hw1(r1, r2)
double precision r1, r2
hw1  = sin(r1+r2)
return
end

subroutine hw2(r1, r2, s)
double precision r1, r2, s
!f2py  intent(out) s
s=sin(r1 + r2)
return
end
