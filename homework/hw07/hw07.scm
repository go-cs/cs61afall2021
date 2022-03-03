(define (cddr s) (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s)))

(define (caddr s) 
    (car (cdr (cdr s))))

(define (ordered? s) 
    (cond 
        ((or (null? s) (null? (cdr s))) #t)
        ((< (car(cdr s)) (car s)) #f)
        (else (ordered? (cdr s))))

    ; (if (or (null? s) (null? (cdr s)))
    ;     #t
    ;     (and (<= (car (cdr s)) (car(cdr s))) 
    ;          (ordered? (cdr s))))

)

(define (square x) (* x x))

(define (pow base exp) 
    (cond ;cond前是一个圆括号
        ((= exp 0) 1)
        ((= base 1) 1)
        ((= exp 1) base)
        ((even? exp) (square (pow base (/ exp 2))))
        (else        (* base (pow base (- exp 1))))
        ))
