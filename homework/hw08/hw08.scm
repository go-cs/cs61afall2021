(define (my-filter func lst) 
    ; (if (null? lst) ni)
    ;     (if (func (car lst)) (cons (car lst)(my-filter func (cdr lst))))
    (cond ((null? lst) nil)
        ((func (car lst)) (cons (car lst) (my-filter func (cdr lst))))
        (else (my-filter func (cdr lst)))
    )
)

(define (interleave s1 s2) 
    (cond ((null? s1) s2)
          ((null? s2) s1)
          (else       (cons (car s1) (cons (car s2) (interleave (cdr s1) (cdr s2))))))
)

(define (accumulate merger start n term)
    ; (if (= n 0) 
    ;     start
    ;     (accumulate merger
    ;                 (merger start (term n))
    ;                 (- n 1)
    ;                 term
    ;     )
    ; )
    (if (>= n 1)
        (accumulate merger (merger start (term n)) (- n 1) term)
        start
    )
)

(define (no-repeats lst) 
    ; (cond ((null? lst) nil)
    ;     ((null? (cdr lst)) lst)
    ;     (= (car lst) (car (cdr lst))) (cons (car lst )(no-repeats (cdr (cdr lst))))
    ;     (else        (cons (car lst) (cdr lst)))
    ; )
    (if (null? lst)
        nil
        (cons (car lst)
            (no-repeats 
                (filter 
                    (lambda(x) 
                        (not (= (car lst) x))
                    )
                    (cdr lst)
                )
            )    
        )
    )
        
)
